# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'lacharogne'

# available languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'es': 'Español'
}

# books export directory
EXPORT_DIR = os.path.join(_basedir, 'files')
# Allowed cover image types
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# Maximum size for each image
MAX_CONTENT_LENGTH = 1 * 1024 * 1024
UPLOADS_COVERS_DEST = os.path.join(_basedir, 'files/covers/')

# Change this line to match your settings
# For dev purposes, an example with sqlite, comes in handy :)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'downpub.db')
# SQLALCHEMY_DATABASE_URI = 'mysql:////downpub:downpub@localhost/downpub'
# migration files will be stored in that directory
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = "True"

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'troispetitstoursetpuissenvont'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LfECu4SAAAAAOipCtoiozremJXlj6t3vUHpl5bI'
RECAPTCHA_PRIVATE_KEY = '6LfECu4SAAAAAM6On_H1FY6cfes9sjl9KQuLqksg'
RECAPTCHA_OPTIONS = {'theme': 'blackglass'}
