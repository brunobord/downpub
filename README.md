DownPub
===========

Free and opensource clone of Editorially, who will soon be deceased. It uses a lot of existing tools ([Epic Editor](http://www.epiceditor.com), [Flask](http://flask.pocoo.org/), [KNACSS](http://www.knacss.com), ...) but all I wrote myself is under [What The Fuck Public Licence](http://www.wtfpl.net/about/)

##Installation

You must install python3, because Downpub will not work well on python2. You must install setuptools too, then - it's optional -
virtualenv. Then, in the virtualenv (or not), enter this :

    pip install Flask Flask-WTF Flask-sqlalchemy Flask-Migrate Flask-Babel

or you can use the provided ``requirements.pip`` file :

    pip install -r requirements.pip

Go to the directory where manage.py is, and type :

    python manage.py db upgrade

This creates and initializes the db

Then, start the webapp :

    python run.py

Now open your browser and go to http://localhost:5000. I'm not yet at ease with web servers and stuff for python (I'm a php dev mostly), but I will try to put a little help around here. Stay tuned.

## But it's broken !

That's normal. Someone told me one day "Release early, release often".

So be it. Besides, even if it's wrong, i'm using git like a sync tool between my home computer and the office one, without any use of branches. Boooh, it's bad, make me bad. Or not.

Just give me some time : I'm learning Python, I'm learning Flask, and I'm learning git. One day it will work. I promise.nne sans fioritures. J'espère.

## The End

Voilà.