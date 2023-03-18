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