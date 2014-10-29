# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'lacharogne'

# available languages
LANGUAGES = {
    'de': 'Deutsh',
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
    'pt': 'Portuguese'
}
# Default locale and timezone
BABEL_DEFAULT_LOCALE = 'fr'
BABEL_DEFAULT_TIMEZONE = 'UTC'

# books export directory
EXPORT_DIR = os.path.join(_basedir, 'downpub', 'files', 'exports')
# books templates directory
TEMPLATE_DIR = os.path.join(_basedir, 'downpub', 'static', 'ebook_templates')
# Allowed cover image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# Maximum size for each image
MAX_CONTENT_LENGTH = 0.5 * 1024 * 1024
# Upload folder for covers
UPLOAD_FOLDER = os.path.join(_basedir, 'downpub', 'files', 'covers')

# Change this line to match your settings
# For dev purposes, an example with sqlite, comes in handy :)
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
