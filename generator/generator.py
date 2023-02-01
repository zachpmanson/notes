import os
from pprint import pprint
import re

import jinja2
import markdown

ignore_names = [
    ".obsidian",
    "Media"
]

# node: {
#   "parent":parentnode,
#   "children":[child1, child2]}
# }
tree = {
    "notes":{
        "parent": None,
        "children": []
    }
}
routes = {}



def get_tree():
    for (root,dirs,files) in os.walk('./notes', topdown=True):
        if (root == ".") or root.split("/")[-1] in ignore_names:
            continue

        title = root.split("/")[-1]
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
    print(tree.keys())
    
    # Generate parents
    queue = ["notes"]
    for node in queue:
        children = tree[node]["children"]
        
        for child in children:
            if node == child:
                continue

            tree[child]["parent"] = node
            queue.append(child)

    

def traverse_tree():
    post_template = jinja2.Template(open("generator/template.jinja", "r").read())

    queue = [*tree["notes"]["children"]]
    for node in queue:

        children = tree[node]["children"]

        parent = tree[node]["parent"]
        siblings = tree[parent]["children"]
        grandparent = tree[parent]["parent"] if parent != None else None
        piblings = tree[grandparent]["children"] if grandparent != None else []
        
        for child in children:
            if node != child:
                queue.append(child)
        try:
            
            with open(os.path.join(routes[node], node+".md"), "r") as src_file:
                text = src_file.read()
                text = re.sub(r"(?<!!)\[\[(.*)\]\]", "[\\1](\\1.html)",text)
                text = re.sub(r"!\[\[(.*)\]\]", "![](Media/\\1)",text)
                body = markdown.markdown(
                    text,
                    extensions=['fenced_code', "codehilite", 'md_in_html', 'toc']
                )
        except FileNotFoundError:
            body = ""

        with open(os.path.join("site", f"{node}.html"), "w") as f:
            f.write(post_template.render({
                "body":body,
                "children": children,
                "siblings": siblings,
                "piblings": piblings
            }))
        print(f"Generated {grandparent}/{parent}/{node}.html")
        # print(siblings)

            




def generate_page(pagename):
    pass

if __name__=="__main__":
    get_tree()
    pprint(tree)
    # pprint(routes)
    traverse_tree()