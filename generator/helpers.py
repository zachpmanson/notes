# Self contained helper functions

from datetime import datetime
import sys


def sanitize_anchor(anchor):
    clean_anchor = anchor.lower()
    clean_anchor = clean_anchor.replace(" ", "-")
    return clean_anchor


def sanitize_url(url):
    """Converts page name to usable URL"""
    clean_url = url.lower()

    if clean_url == "index":
        clean_url = ""
    elif clean_url == "404":
        clean_url = "404.html"
    else:
        subs = {" ": "-", '"': "", "'": "", ",": "", "&": "and"}
        for key, value in subs.items():
            clean_url = clean_url.replace(key, value)

    return clean_url


def usage():
    print("usage: generator.py [-v]", file=sys.stderr)


def format_recent_edit(tree, i):
    page_name = sorted(tree, key=lambda x: tree[x]["mod_date"], reverse=True)[int(i)]
    return f"{tree[page_name]['mod_date']}: [[{page_name}]]"


def random_js(tree):
    return f"""
        let list = {list(map(sanitize_url, tree.keys()))};
        window.location.replace("/"+list[Math.floor(Math.random() * list.length)]);
    """


def tags_js():
    return """
        let tag = window.location.hash.slice(1);
        let details = document.getElementById(tag).parentElement.parentElement; // id is attached to h2, not details
        details.open = true;
    """
