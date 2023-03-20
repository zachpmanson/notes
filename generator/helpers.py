from datetime import datetime

# Self contained helper functions

def sanitize_anchor(anchor):
    clean_anchor = anchor.lower()
    clean_anchor = clean_anchor.replace(" ", "-")
    return clean_anchor

def sanitize_url(url):
    url = url.lower()
    if url == "index":
        clean_url = ""
    else:
        clean_url = url.replace(" ", "-").replace('"', '')
        
    return clean_url

def usage():
    print("usage: generator.py [-v]", file=sys.stderr) 

def format_recent_edit(tree, i):
    page_name = sorted(tree, key=lambda x:tree[x]["mod_time"], reverse=True)[int(i)]
    date = datetime.utcfromtimestamp(tree[page_name]['mod_time']).strftime('%Y-%m-%d %H:%M:%S')
    # return f"[[{page_name}]] - {datetime.utcfromtimestamp(tree[page_name]['mod_time']).strftime('%Y-%m-%d %H:%M:%S')}"
    return f"{date} - [[{page_name}]]"