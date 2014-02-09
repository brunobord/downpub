DownPub
===========

Projet de clone libre d'Editorially. Sera sûrement jamais fini par moi-même, utilise des librairies externes ([Epic Editor](http://www.epiceditor.com), [Flask](http://flask.pocoo.org/), [KNACSS](http://www.knacss.com), ..), mais le contenu que moi j'ai codé est en [What The Fuck Public Licence](http://www.wtfpl.net/about/)

##Installation

Installez python, setuptools, (éventuellement virtualenv) puis (dans le virtualenv ou pas) :

1. pip install Flask
2. pip install Flask-WTF
3. pip install Flask-sqlalchemy
3. pip install Flask-Migrate

Ensuite, une fois dans le dossier où se trouve le script manage.py lancez :

1. python manage.py db upgrade

Cela initialise et crée la bdd.

Enfin, lancez le fichier run.py via python

1. python run.py

Accédez alors à l'appli via (http://localhost:5000). Pour plus d'infos sur la façon d'installer ça derrière un serveur web, je... ne sais pas pour l'instant, mais ça peut se faire avec nginx et uwsgi, par exemple. À vous de voir, j'suis encore un peu perdu dans tout ça.

## Mais c'est tout cassé !

Normal. Quelqu'un m'a dit "Release early, release often".

Donc je prend au pied de la lettre. De plus - et c'est mal - je me sers de git comme d'un sync entre mes pc de boulot et maison, sans me faire chier à créer des branches. Bouh c'est mal, fouettez-moi. Ou pas.

Mais avec le temps, chaque chose sera corrigée, et j'espère dans les mois qui viennent avoir un truc de base qui fonctionne sans fioritures. J'espère.

## Mot de la fin

Voilà.