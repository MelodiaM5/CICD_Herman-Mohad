try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

def listmenus(url,id):
    SUP_URL = urljoin(url, '{'+id+'}')
    r = requests.get(url)

    json = r.json()
    print(json)
    if r.ok:
        return r
    else:
        return None