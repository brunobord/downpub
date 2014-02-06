import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['paindesegle@gmail.com'])
SECRET_KEY = 'lacharogne'

# available languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'es': 'Español'
}

# Changez cette ligne pour une ligne correspondante à la bdd que vous utilisez
# Voici un exemple sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'downpub.db')
# SQLALCHEMY_DATABASE_URI = 'mysql:////downpub:downpub@localhost/downpub'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = "True"

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'troispetitstoursetpuissenvont'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LfECu4SAAAAAOipCtoiozremJXlj6t3vUHpl5bI'
RECAPTCHA_PRIVATE_KEY = '6LfECu4SAAAAAM6On_H1FY6cfes9sjl9KQuLqksg'
RECAPTCHA_OPTIONS = {'theme': 'blackglass'}
