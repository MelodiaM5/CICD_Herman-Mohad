""" Functions to list teh menus from the server """
#--- Librairies -------------------------------------------------#
import requests

#--- functions --------------------------------------------------#
def listmenus(url):
    """
        Functions to list all the menus
        url: url to the website
        type: string
        return: menus 
        type: string
    """
    r = requests.get(url)
    json = r.json()
    menu_layout = rewrite(json)
    return menu_layout

def rewrite(json):
    """
        Functions to transforme the menus to a human readable menus
        json: text to transform
        type: json
        return: text readable for a human 
        type: string
    """
    if len(json)==0:
        return "There is no menu yet"
    else:
        menus_result = ""
        for i in range(len(json)):
            menus_result += str(json[i].get("id")) + " "
            menus_result += str(json[i].get("name")) + "\n"
            for j in range(len(json[i].get("dishes"))):
                menus_result += "   " + json[i].get("dishes")[j].get("name") + "\n"

        return menus_result 