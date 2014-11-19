# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
from flask.ext.babel import gettext

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

VERSION = "0.0.0.1"

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

part_content = gettext("# Chapter 1 - Introducing Downpub") \
    + "\n\n" \
    + gettext("This is a demo text which contains _examples_ on __how__ to use ___Markdown___ syntax to format your book.") \
    + "\n\n" \
    + gettext("## SubChapter 1 - Text Formatting, almost WYSIWYG") \
    + "\n\n" \
    + gettext("In this section, we'll have a look at making text **bold**, *italic* and etc. If you haven't realised by now, there is a very simple toolbar presented above the editor. Try selecting text in this editor and press any one of those buttons.") \
    + "\n\n" \
    + gettext("1. Item1") + '\n' \
    + gettext("1. Item2") + '\n' \
    + gettext("1. Item3") \
    + "\n\n" \
    + "!["+gettext('Even my cat can be in your epub !')+"](https://farm3.staticflickr.com/2756/4290352584_9d92fedfe2_z_d.jpg)" + '\n' \
    + "\n\n" \
    + gettext("- Item1") + '\n' \
    + gettext("- Item2") + '\n' \
    + gettext("- Item3") \
    + "\n\n" \
    + gettext("### Example source code") \
    + "\n\n" \
    + "```" + '\n' \
    + "print('Holy code of doom and destruction')" + '\n' \
    + "```" + '\n' \
    + "\n\n" \
    + gettext("Take a peek at those buttons and see how they work !") + '\n' \
    + "\n\n" \
    + gettext("Don't hesitate to export the book in epub or watch the preview to see what you wrote looks like.") + '\n'

DEFAULT_PART_CONTENT = part_content

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
