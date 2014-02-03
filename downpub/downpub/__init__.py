from functools import wraps
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel

downpub = Flask(__name__)
downpub.config.from_object('config')

db = SQLAlchemy(downpub)
babel = Babel(downpub)

@downpub.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@downpub.route('/')
def index():
  return render_template("index.html")


from downpub.users.views import mod as usersModule
from downpub.books.views import mod as booksModule
downpub.register_blueprint(usersModule)
downpub.register_blueprint(booksModule)
