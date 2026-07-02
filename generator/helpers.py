# Self contained helper functions

import sys
import unicodedata

from generator.types import Node


def sanitize_url(url):
    """Converts page name to usable URL"""
    clean_url = unicodedata.normalize("NFD", url)

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
    page_name = sorted(tree, key=lambda x: tree[x].mod_date, reverse=True)[int(i)]
    return f"{tree[page_name].mod_date}: [[{page_name}]]"


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


def chronological_tag(tag: str, tag_pages: list[str], tree: dict[str, Node]):
    nodes = {page: tree[page] for page in tag_pages if tree[page].post_date}
    nodes = dict(
        sorted(nodes.items(), key=lambda item: item[1].post_date, reverse=True)
    )
    html = []
    for page, node in nodes.items():
        # html += [f"{node.post_date}: [{page}](/{sanitize_url(page)})"]
        html += [
            f"<div class='post'><a href='/{sanitize_url(page)}'>{page}</a>  <time>{node.post_date}</time></div>"
        ]
    return (
        "\n".join(html)
        + f"<a href='/{tag}.xml'>RSS Feed</a> | <a href='feed://notes.zachmanson.com/{tag}.xml'>Subscribe</a>"
    )


def inline_tag(
    tag: str,
    tag_pages: list[str],
    tree: dict[str, Node],
    show_title: str,
    chronological: bool,
):
    if chronological:
        nodes = {page: tree[page] for page in tag_pages if tree[page].post_date}
    else:
        nodes = {page: tree[page] for page in tag_pages}

    def sort_by_post_date(item):
        return item[1].post_date

    def sort_by_title(item):
        return item[1].title.lower()

    sort_fn = sort_by_post_date if chronological else sort_by_title

    nodes = dict(sorted(nodes.items(), key=sort_fn, reverse=True))

    html = []
    render_title = show_title == "show-title"

    for page, node in nodes.items():
        # Exclude the page with the same name as the tag
        if sanitize_url(node.title) == sanitize_url(tag):
            continue

        element = "\n"
        if render_title:
            element += f"<h1>{node.subtitle or node.title}</h1>\n"

        element += node.body
        element += f"\n\n<a href='/{sanitize_url(node.title)}'>⌾</a>"
        html.append(element)

    return "<br><br>".join(html)
