import os
import re
from datetime import datetime
import getopt
import sys

import jinja2
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

import helpers

VERBOSE = False

md_extensions = [
    'fenced_code',
    CodeHiliteExtension(guess_lang=False),
    'md_in_html',
    'toc',
    'pymdownx.superfences',
    'markdown_checklist.extension',
    'md_in_html'
]

ignore_names = [
    ".obsidian",
    "Media",
    ".trash"
]

ochrs_vars = {
    "ochrs-vars": lambda: ", ".join(list(ochrs_vars.keys())),
    "example": lambda: "<ochrs:var-name>",
    "page-count": lambda: len(tree),
    "build-time": lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "md-extensions": lambda: ", ".join([e if isinstance(e, str) else str(type(e).__name__) for e in md_extensions]),
    "recent-edit": lambda i: helpers.format_recent_edit(tree, i)
}

# node: {
#   "parent":parentnode,
#   "children":[child1, child2]},
#   "body":""
#   "backlinks":[]
#   "mod_time": mod_time
# }
tree = {
    "Index": {
        "parent": None,
        "children": [],
        "body":"",
        "backlinks":[],
        "mod_time": 0.0
    }
}
routes = {
    "Index": "./"
}

# {node: ["link1", "link2"]}
backlinks = {}

sitemap_md = ""
current_node = "Index"

def get_tree():
    if VERBOSE: print("Building tree")
    for (root,dirs,files) in os.walk('./notes', topdown=True):
        if (root == "."):
            continue
        
        on_ignore = False
        for segment in root.split("/"):
            if segment in ignore_names:
                on_ignore = True
        if on_ignore:
            if VERBOSE: print("Skipping", root)
            continue


        title = root.split("/")[-1]
        if title == "notes":
            title = "Index"
        # print(title,tree[title])

        for file in files:
            if file in ignore_names:
                continue
            if file[:-3] == root:
                continue
            if not file.endswith(".md"):
                continue
            
            page_name = file[:-3]
            try:
                tree[page_name]["children"]
            except KeyError:
                tree[page_name] = {"children":[]}

            if title != page_name:
                tree[title]["children"].append(page_name)

            routes[page_name] = root
        
        for dirname in dirs:
            if dirname in ignore_names:
                continue
            
            tree[title]["children"].append(dirname)
            try:
                tree[dirname]["children"]
            except KeyError:
                tree[dirname] = {"children":[]}

            routes[dirname] = root
    
    # Generate parents and backlinks
    queue = ["Index"]
    for node in queue:
        (tree[node]["children"]).sort()
        children = tree[node]["children"]
        tree[node]["backlinks"] = []
        tree[node]["body"] = ""
        try:
            path = os.path.join(routes[node], node+".md")
            mod_time = os.path.getmtime(path)
        except FileNotFoundError:
            mod_date = 0.0
        tree[node]["mod_time"] = mod_time

        for child in children:
            if node == child:
                continue

            tree[child]["parent"] = node
            queue.append(child)

def traverse_tree():
    global current_node

    # generate page bodies and record backlinks
    for node in tree.keys():
        current_node = node
        try:
            path = os.path.join(routes[node], node+".md")
            with open(path, "r") as src_file:
                text = src_file.read()
                text = preprocess_markdown(text)
                body = markdown.markdown(
                    text,
                    extensions=md_extensions
                )
        except FileNotFoundError:
            body = ""
            mod_date = 0.0
        tree[node]["body"] = body

def generate_pages():
    post_template = jinja2.Template(open("generator/template.jinja", "r").read())
    # actually generate pages
    for node in tree.keys():
        children = tree[node]["children"]

        parent = tree[node]["parent"]
        siblings = tree[parent]["children"] if parent != None else None
        grandparent = tree[parent]["parent"] if parent != None else None
        piblings = tree[grandparent]["children"] if grandparent != None else None

        if node != "Index":
            path = os.path.join("site", helpers.sanitize_url(node))
        else:
            path = "site"

        if not os.path.exists(path):
            os.mkdir(path)

        with open(os.path.join(path, "index.html"), "w") as f:
            f.write(post_template.render({
                "title": node,
                "body": tree[node]["body"],
                "parent": parent,
                "children": children,
                "siblings": siblings,
                "piblings": piblings,
                "len": len,
                "sanitize_url": helpers.sanitize_url,
                "backlinks": [*set(tree[node]["backlinks"])],
                "last_edit": str(datetime.utcfromtimestamp(tree[node]["mod_time"]).strftime('%Y-%m-%d %H:%M:%S'))
            }))
        if VERBOSE: print(f"Generated {grandparent}/{parent}/{helpers.sanitize_url(node)}/index.html")


def generate_sitemap():
    global sitemap_md
    # generate some markdown
    sitemap_md += "Last build at <ochrs:build-time>. This site currently has <ochrs:page-count> pages.\n\n"
    sitemap_md += "- [Index](/)\n"
    for node in tree["Index"]["children"]:
        append_bullet(node, 4)
    
    sitemap_md = preprocess_markdown(sitemap_md)
    post_template = jinja2.Template(open("generator/template.jinja", "r").read())
    sitemap_html = markdown.markdown(
        sitemap_md,
        extensions=md_extensions
    )
    with open(os.path.join("site", "404.html"), "w") as f:
        f.write(post_template.render({
            "title": "Sitemap",
            "body": sitemap_html,
            "parent": "Index",
            "children": None,
            "siblings": tree["Index"]["children"],
            "piblings": None,
            "len": len,
            "sanitize_url": helpers.sanitize_url,
            "backlinks": []
        }))
    if VERBOSE: print("Generated sitemap")

def append_bullet(node, depth):
    global sitemap_md
    sitemap_md += f"{' ' * depth}- [{node}](/{helpers.sanitize_url(node)})\n"

    for child in tree[node]["children"]:
        append_bullet(child, depth+4)

def preprocess_markdown(text):
    # add ochrs vars
    text = re.sub(r"<ochrs:(.+?)>", format_ochrs_var, text)
    # add backlinks
    text = re.sub(r"(?<!!)\[\[([^\]]+)?\]\]", format_backlink, text)
    # add images backlink
    text = re.sub(r"!\[\[([^\]]+)?\]\]", "![](/static/media/\\1)", text)
    return text

def format_ochrs_var(matches):
    try:
        segments = matches.group(1).split(":")
        name = segments[0]
        if len(segments) > 1:
            args = segments[1:]
        else:
            args = []
        value = str(ochrs_vars[name](*args))
    except KeyError as e:
        print("KeyError:", e)
        value = "unknown ochrs var"
    return value

def format_backlink(matches):
    if "|" in matches.group(1):
        segments = matches.group(1).split("|")
        text = segments[1]
        page = segments[0]
    else:
        text = matches.group(1)
        page = text
    
    anchor = ""

    if "#" in page:
        segments = page.split("#")
        page = segments[0]
        anchor = f"#{helpers.sanitize_anchor(segments[1])}"

    # if they are capitalised differently, fix it 
    if page not in routes.keys():
        for key in routes.keys():
            if page.lower() == key.lower():
                page = key
                break

    tree[page]["backlinks"].append(current_node)

    return f"[{text}](/{helpers.sanitize_url(page)}{anchor})"

if __name__=="__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "v")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        helpers.usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-v":
            VERBOSE = True
    get_tree()
    traverse_tree()
    generate_pages()
    generate_sitemap()
