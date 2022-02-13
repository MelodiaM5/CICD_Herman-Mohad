import requests


def listmenus(url):
    r = requests.get(url)
    json = r.json()
    print(json)
    if r.ok:
        return r
    else:
        return None