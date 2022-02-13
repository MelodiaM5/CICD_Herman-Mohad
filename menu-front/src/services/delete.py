try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

def delete(url,id):
    idString = 'menus/' + id
    SUP_URL = urljoin(url, idString)
    r = requests.delete(SUP_URL)

    return r
