import requests as rq

def listmenus(url):
    r = rq.get(url)
    json = r.json()
    menu_layout = rewrite(json)
    return menu_layout

def rewrite(json):
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