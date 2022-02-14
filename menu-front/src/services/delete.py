""" Code to delete menus """

#--- librairies -------------------------------------------------#
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

#--- Functions ---------------------------------------------------#
def delete(url,id):
    """
        Function to delete a menus
        url: url where the request should be done
        type: string
        id: id to the menu to delete
        type: string
        return: reponse to the server
    """
    idString = 'menus/' + id
    SUP_URL = urljoin(url, idString)
    r = requests.delete(SUP_URL)

    return r
