import os
from pprint import pprint
import re

import jinja2
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

ignore_names = [
    ".obsidian",
    "Media"
]

# node: {
#   "parent":parentnode,
#   "children":[child1, child2]},
#   "body":""
#   "backlinks":[]
# }
tree = {
    "Index": {
        "parent": None,
        "children": [],
        "body":"",
        "backlinks":[]

    }
}
routes = {
    "Index": "./"
}

# {node: ["link1", "link2"]}
backlinks = {}

current_node = "Index"

def get_tree():
    for (root,dirs,files) in os.walk('./notes', topdown=True):
        if (root == ".") or root.split("/")[-1] in ignore_names:
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
        children = tree[node]["children"]
        tree[node]["backlinks"] = []
        tree[node]["body"] = ""
        
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
            with open(os.path.join(routes[node], node+".md"), "r") as src_file:
                text = src_file.read()
                text = re.sub(r"(?<!!)\[\[([^\]]+)?\]\]", format_backlink, text)
                text = re.sub(r"!\[\[([^\]]+)?\]\]", "![](/static/media/\\1)", text)
                body = markdown.markdown(
                    text,
                    extensions=['fenced_code', CodeHiliteExtension(guess_lang=False), 'md_in_html', 'toc']
                )
        except FileNotFoundError:
            body = ""
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
            path = os.path.join("site", sanitize_url(node))
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
                "sanitize_url": sanitize_url,
                "backlinks": tree[node]["backlinks"]
            }))
        print(f"Generated {grandparent}/{parent}/{sanitize_url(node)}/index.html")


def format_backlink(matches):
    if "|" in matches.group(1):
        segments = matches.group(1).split("|")
        text = segments[1]
        page = segments[0]
    else:
        text = matches.group(1)
        page = text
    
    # if they are capitalised differently, fix it 
    if page not in routes.keys():
        for key in routes.keys():
            if page.lower() == key.lower():
                page = key
                break

    tree[page]["backlinks"].append(current_node)

    return f"[{text}](/{sanitize_url(page)})"
        
def sanitize_url(url):
    if url.lower() == "index":
        clean_url = ""
    else:
        clean_url = url.replace(" ", "_").replace('"', '')
        
    return clean_url

if __name__=="__main__":
    get_tree()
    traverse_tree()
    generate_pages()