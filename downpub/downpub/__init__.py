# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask import Flask, render_template, g, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel, gettext
from config import *
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


downpub = Flask(__name__)
downpub.config.from_object('config')
downpub.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(downpub)
babel = Babel(downpub)

migrate = Migrate(downpub, db)

manager = Manager(downpub)
manager.add_command('db', MigrateCommand)


@babel.localeselector
def get_locale():
    """
    Returns user's locale or the best match based on your browser's settings
    """
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale

    return request.accept_languages.best_match(list(LANGUAGES.keys()))


@babel.timezoneselector
def get_timezone():
    """
    Returns user timezone or None
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

from downpub.users.models import User


@downpub.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
        if not g.user is None:
            g.user_id = session['user_id']
            g.locale = g.user.locale


@downpub.errorhandler(404)
def not_found(error):
    """
    Handling 404 errors
    """
    return render_template('404.html', user=g.user), 404


@downpub.errorhandler(413)
def file_too_big(error):
    """
    Handling 413 "file too big" errors
    """
    return render_template('413.html', user=g.user), 413


@downpub.errorhandler(500)
def error_500(error):
    """
    Handling 500 errors
    """
    return render_template('500.html', user=g.user), 500


@downpub.route('/')
def index():
    return render_template("index.html",
        user=g.user, site_title=gettext("Home"))


from downpub.users.views import mod as usersModule
from downpub.books.views import mod as booksModule
downpub.register_blueprint(usersModule)
downpub.register_blueprint(booksModule)
