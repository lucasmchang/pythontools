import urllib.request

def scrape(url, handle_cookies = True):
    if handle_cookies:
        handler = urllib.request.HTTPCookieProcessor()
        opener = urllib.request.build_opener(handler)
        data = opener.open(url)
    else:
        data = urllib.request.urlopen(url)
    return data.read().decode('utf-8')
