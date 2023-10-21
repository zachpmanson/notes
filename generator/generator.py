import os
import re
from datetime import datetime
import getopt
import sys
import random

import jinja2
import markdown
import frontmatter
from markdown.extensions.codehilite import CodeHiliteExtension

from extensions.cite import CiteExtension
from extensions.backlink import BacklinkExtension

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
    
    global current_node
    
    # Generate parents and backlinks
    queue = ["Index"]
    for node in queue:
        current_node = node
        # (tree[node]["children"]).sort()
        # children = sorted(list(tree[node]["children"]))
        tree[node]["backlinks"] = set()
        tree[node]["body"] = ""
        try:
            path = os.path.join(routes[node], node+".md")
            mod_time = os.path.getmtime(path)
            with open(path, "r") as src_file:
                file_sections = frontmatter.load(src_file)
                body = file_sections.content

                if "tags" in list(file_sections.keys()):
                    format_tags(file_sections["tags"])

        except FileNotFoundError:
            mod_time = 0.0
            body = "🌱"
        
        tree[node]["body"] = body
        tree[node]["mod_time"] = mod_time
        tree[node]["breadcrumb_path"] = path

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
        tree[node]["body"] = preprocess_markdown(tree[node]["body"])
        tree[node]["body"] = process_markdown(tree[node]["body"])

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
        
        page_tags = [tagname for tagname, tagpages in tags.items() if node in tagpages]
        with open(filename, "w") as f:
            f.write(post_template.render({
                "title": node,
                "body": tree[node]["body"],
                "parent": parent,
                "children": children,
                "siblings": siblings,
                "piblings": piblings,
                "tags": page_tags,
                "len": len,
                "sanitize_url": helpers.sanitize_url,
                "backlinks": tree[node]["backlinks"],
                "breadcrumb_path": tree[node]["breadcrumb_path"],
                "last_edit": str(datetime.utcfromtimestamp(tree[node]["mod_time"]).strftime('%Y-%m-%d %H:%M:%S')),
                "random_page": tree[node]["random_page"]
            }))

        if VERBOSE: print(f"Generated {grandparent}/{parent}/{helpers.sanitize_url(node)}/index.html")

def generate_sitemap():
    global sitemap_md

    append_bullet("Index", 0)
    
    if VERBOSE: print("Generated sitemap\n", sitemap_md)
    return sitemap_md

def generate_random_pages():
    random_pages = list(tree.keys())
    random.shuffle(random_pages)

    for i in range(len(random_pages)):
        tree[random_pages[i]]["random_page"] = random_pages[(i + 1) % len(random_pages)]

def append_bullet(node, depth):
    global sitemap_md
    sitemap_md += f"{' ' * depth}- [{node}](/{helpers.sanitize_url(node)})\n"

    for child in sorted(tree[node]["children"]):
        append_bullet(child, depth+4)

def generate_tags():
    global tags_md
    tags_md = ""
    for tag in sorted(tags.keys()):
        pages = sorted(tags[tag])
        panel = f"<details markdown='1'><summary>\n## {tag}\n</summary>\n\n"
        panel += "\n".join([f"- [{page}](/{helpers.sanitize_anchor(page)})" for page in pages])
        panel += "\n</details>\n"

        tags_md += panel

def preprocess_markdown(text):
    # TODO: Move this to a seperate md extension
    # add ochrs functions
    text = re.sub(r"<ochrs:(.+?)>", format_ochrs_func, text)
    
    # TODO: Move this to a seperate md extension
    # add images backlink
    text = re.sub(r"!\[\[([^\]]+)?\]\]", "![](/media/\\1)", text)

    return text

def process_markdown(text):
    processed_text = markdown.markdown(
        text,
        extensions=md_extensions
    )
    return processed_text

def propagate_tags():
    '''Apply tag to all children of a page that matches a tag name''' 
    for key in tree.keys():
        if helpers.sanitize_url(key) in tags.keys():
            queue = list(tree[key]["children"])
            tags[helpers.sanitize_url(key)].add(key)

            for page in queue:
                for child in tree[page]["children"]:
                    queue.append(child)
                tags[helpers.sanitize_url(key)].add(page)

def format_tags(taglist):
    '''Formats tags and adds them to the tags object'''
    global current_node
    # formatted_tags = []
    for tag in taglist:
        if tag in tags.keys():
            tags[tag].add(current_node)
        else:
            tags[tag] = set()
            tags[tag].add(current_node)

def format_ochrs_func(matches):
    try:
        segments = matches.group(1).split(":")
        name = segments[0]
        if len(segments) > 1:
            args = segments[1:]
        else:
            args = []
        value = str(ochrs_funcs[name](*args))
    except KeyError as e:
        print("KeyError:", e, file=sys.stderr)
        value = "unknown ochrs func"
    return value


VERBOSE = False

def build_backlink(label, base, end):
    
    anchor = ""
    page = label
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
    
    # ignore links from lectures
    if not re.match(r"W[0-9]{2}L[0-9]{2}", current_node):
        tree[page]["backlinks"].add(current_node)

    page = helpers.sanitize_url(page)
    
    return base+page+end+anchor


md_extensions = [
    'fenced_code',
    BacklinkExtension(
        build_url=build_backlink,
        html_class="",
        end_url=""
    ),
    CodeHiliteExtension(guess_lang=False),
    'md_in_html',
    'toc',
    'tables',
    'pymdownx.superfences',
    'markdown_checklist.extension',
    CiteExtension()
]

ignore_names = [
    ".obsidian",
    "Media",
    ".trash"
]

ochrs_funcs = {
    "ochrs-funcs": lambda: ", ".join(list(ochrs_funcs.keys())),
    "example": lambda: "<ochrs:func-name:arg1:arg2>",
    "page-count": lambda: len(tree),
    "build-time": lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "md-extensions": lambda: ", ".join([e if isinstance(e, str) else str(type(e).__name__) for e in md_extensions]),
    "recent-edit": lambda i: helpers.format_recent_edit(tree, i),
    "sitemap": lambda: sitemap_md,
    "tags": lambda: tags_md
}

# node: {
#   "parent":parentnode,
#   "children":[child1, child2]},
#   "body":""
#   "backlinks":[]
#   "mod_time": mod_time
#   "breadcrump_path": path in notes folder as string
# }
tree = {
    "Index": {
        "parent": None,
        "children": set(),
        "body":"",
        "backlinks":set(),
        "mod_time": 0.0,
        "breadcrump_path":"Index.md",
        "random_page": ""
    }
}
routes = {
    "Index": "./"
}

# { tagname: ["link1", "link3"]}
tags = {}
tags_md = "Tags not generated yet"
# {node: ["link1", "link2"]}
# backlinks = {}

sitemap_md = ""
current_node = "Index"

orphans = ["404"]

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
    propagate_tags()
    generate_tags()
    generate_sitemap()
    traverse_tree()
    generate_random_pages()
    generate_pages()
    
    # for l in tree.keys():
    #     del tree[l]["body"]
    #     print(l)
    #     pprint(tree[l])
