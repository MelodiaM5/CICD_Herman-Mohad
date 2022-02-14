# Outil d'interrogation d'api Menufront.py 

Bienvenue sur l'aide d'installation de l'outil Python d'interrogation d'api menu-server.

# Installation

Pour que notre outil fonctionne correctement, python3.9.10 est conseillé.

Après avoir téléchargé et décompressé l'archive, lancer la suite de commandes suivantes: 

`cd menu-front/src` <br/>
`python -m pip install --upgrade pip`<br/>
`pip install -r requirements.txt`

# Utilisation

Notre ligne de commande s'utilise en se plaçant à l'emplacement CICD_Herman-Mohad/menu-front/src/ <br/>
La syntaxe d'utilisation est: <br/>
`python menufront.py`

Les différentes options sont:<br/>
-URL pour définir l'url utilisée par défaut par l'application<br/>
-list pour demander le listing des menus existants<br/>
-delete id pour delete l'id donné par l'utilisateur<br/>
-h pour afficher les différents paramètres<br/>
