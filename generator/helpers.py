from datetime import datetime

# Self contained helper functions

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
        subs = {
            " ":"-",
            '"':"",
            "'":"",
            ",":"",
            "&":"and"
        }   
        for key,value in subs.items():
            clean_url = clean_url.replace(key, value)
        
    return clean_url

def usage():
    print("usage: generator.py [-v]", file=sys.stderr) 

def format_recent_edit(tree, i):
    page_name = sorted(tree, key=lambda x:tree[x]["mod_time"], reverse=True)[int(i)]
    date = datetime.utcfromtimestamp(tree[page_name]['mod_time']).strftime('%Y-%m-%d')
    return f"{date}: [[{page_name}]]"

def random_js(tree):
    return f"""
        let list = {list(map(sanitize_url, tree.keys()))};
        window.location.replace("/"+list[Math.floor(Math.random() * list.length)]);
    """