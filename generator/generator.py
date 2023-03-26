import os
import re
from datetime import datetime
import getopt
import sys

import jinja2
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

import helpers

from pprint import pprint

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
                tree[page_name] = {"children":set()}

            if (title != page_name):
                tree[title]["children"].add(page_name)

            routes[page_name] = root
        
        for dirname in dirs:
            if dirname in ignore_names:
                continue
            
            tree[title]["children"].add(dirname)
            try:
                tree[dirname]["children"]
            except KeyError:
                tree[dirname] = {"children":set()}

            routes[dirname] = root
    
    # Generate parents and backlinks
    queue = ["Index"]
    for node in queue:
        # (tree[node]["children"]).sort()
        # children = sorted(list(tree[node]["children"]))
        tree[node]["backlinks"] = set()
        tree[node]["body"] = ""
        try:
            path = os.path.join(routes[node], node+".md")
            mod_time = os.path.getmtime(path)
        except FileNotFoundError:
            mod_time = 0.0
        tree[node]["mod_time"] = mod_time

        for child in tree[node]["children"]:
            if node == child:
                continue

            tree[child]["parent"] = node
            queue.append(child)
    # pprint(tree)

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
                body = process_markdown(text)
        except FileNotFoundError:
            body = ""
        tree[node]["body"] = body

def generate_pages():
    # actually generate pages
    for node in tree.keys():
        children = sorted(list(filter(lambda x: x not in orphans or x == node, tree[node]["children"])))

        parent = tree[node]["parent"]
        siblings = sorted(list(filter(lambda x: x not in orphans or x == node, tree[parent]["children"]))) if parent != None else None
        
        grandparent = tree[parent]["parent"] if parent != None else None
        piblings = sorted(list(filter(lambda x: x not in orphans or x == parent, tree[grandparent]["children"]))) if grandparent != None else None

        if node != "Index":
            path = os.path.join("site", helpers.sanitize_url(node))
        else:
            path = "site"

        # 404 page is special, must be a html page
        if node == "404":
            filename = os.path.join("site", "404.html")
        else:
            if not os.path.exists(path):
                os.mkdir(path)
            filename = os.path.join(path, "index.html")
        
        with open(filename, "w") as f:
            f.write(post_template.render({
                "title": node,
                "body": tree[node]["body"],
                "parent": parent,
                "children": children,
                "siblings": siblings,
                "piblings": piblings,
                "len": len,
                "sanitize_url": helpers.sanitize_url,
                "backlinks": tree[node]["backlinks"],
                "last_edit": str(datetime.utcfromtimestamp(tree[node]["mod_time"]).strftime('%Y-%m-%d %H:%M:%S'))
            }))
        if VERBOSE: print(f"Generated {grandparent}/{parent}/{helpers.sanitize_url(node)}/index.html")

def generate_sitemap():
    global sitemap_md
    # generate some markdown
    sitemap_md += "- [Index](/)\n"
    for node in tree["Index"]["children"]:
        append_bullet(node, 4)
    
    if VERBOSE: print("Generated sitemap")
    return sitemap_md

def generate_tags():
    tags_md = ""
    for tag, pages in tags.items():
        panel = f"<details><summary>\n## {tag}\n</summary>"
        
        panel += "\n".join([f"- [{page}]({helpers.sanitize_anchor(page)})" for page in pages])
        
        panel += "</details>"

        tags_md += panel

    return tags_md

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
    # process tags
    text = re.sub(r"Tags: (.+)", format_tags, text)
    return text

def process_markdown(text):
    processed_text = markdown.markdown(
        text,
        extensions=md_extensions
    )
    return processed_text

def format_tags(matches):
    '''Formats tags and adds them to the tags object'''
    global current_node
    tagline = matches.group(1)
    taglist = tagline.replace("#", "").split()
    formatted_tags = []
    for tag in taglist:
        if tag in tags.keys():
            tags[tag].add(current_node)
        else:
            tags[tag] = set()
        # tree["Tags"]["children"].add(f"tags/{tag}")
        formatted_tags.append(f"[{tag}](/tags/{tag})")

    return "**Tags:** " + " ".join(formatted_tags)
        

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

    tree[page]["backlinks"].add(current_node)

    return f"[{text}](/{helpers.sanitize_url(page)}{anchor})"



VERBOSE = False

md_extensions = [
    'fenced_code',
    CodeHiliteExtension(guess_lang=False),
    'md_in_html',
    'toc',
    'pymdownx.superfences',
    'markdown_checklist.extension',
]

ignore_names = [
    ".obsidian",
    "Media",
    ".trash"
]

ochrs_vars = {
    "ochrs-vars": lambda: ", ".join(list(ochrs_vars.keys())),
    "example": lambda: "<ochrs:var-name:arg1:arg2>",
    "page-count": lambda: len(tree),
    "build-time": lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "md-extensions": lambda: ", ".join([e if isinstance(e, str) else str(type(e).__name__) for e in md_extensions]),
    "recent-edit": lambda i: helpers.format_recent_edit(tree, i),
    "sitemap": generate_sitemap,
    "tags": generate_tags
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
        "children": set(),
        "body":"",
        "backlinks":set(),
        "mod_time": 0.0
    }
}
routes = {
    "Index": "./"
}

# { tagname: ["link1", "link3"]}
tags = {}

# {node: ["link1", "link2"]}
# backlinks = {}

sitemap_md = ""
current_node = "Index"

orphans = ["404"]#, "Tags"]

post_template = jinja2.Template(open("generator/template.jinja", "r").read())


if __name__=="__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "v")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err, file=sys.stderr)  # will print something like "option -a not recognized"
        helpers.usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-v":
            VERBOSE = True
    get_tree()
    traverse_tree()
    generate_pages()


