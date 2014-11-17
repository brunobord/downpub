# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import os.path

from flask.ext.wtf import Form
from wtforms import TextField, StringField, TextAreaField, SelectField
from wtforms.validators import Required, Length
from flask_wtf.file import FileField, FileAllowed
from flask.ext.babel import lazy_gettext

from config import TEMPLATE_DIR, LANGUAGES


class AddForm(Form):
    title = StringField(lazy_gettext('Book title'),
        [Required(), Length(max=80)])
    subtitle = StringField(lazy_gettext('Book subtitle'),
        [Required(), Length(max=255)])
    displayed_name = TextField(lazy_gettext('Displayed author name'),
        [Length(max=255)])
    editor = StringField(lazy_gettext('Book editor'),
        [Required(), Length(max=255)])
    publisher = StringField(lazy_gettext('Book publisher'),
        [Required(), Length(max=255)])
    style = SelectField(
        lazy_gettext('Select your css template !'),
        choices=[(template, template) for template in os.listdir(TEMPLATE_DIR) if os.path.isdir(os.path.join(TEMPLATE_DIR, template))]
        )
    language = SelectField(
        lazy_gettext('Select your language !'),
        choices=sorted([(short, name) for short,name in list(LANGUAGES.items())])
        )
    rights = TextField(lazy_gettext('Displayed Copyright'),
        [Length(max=255)])


class AddCoverForm(Form):
    cover = FileField(lazy_gettext('Image File'),
        [FileAllowed(['jpg', 'jpeg', 'gif', 'png'],
        lazy_gettext('Images only!'))])


class EditForm(Form):
    title = TextField(lazy_gettext('Book title'),
        [Required(), Length(max=80)])
    subtitle = StringField(lazy_gettext('Book subtitle'),
        [Required(), Length(max=255)])
    displayed_name = TextField(lazy_gettext('Displayed author name'),
        [Length(max=255)])
    editor = StringField(lazy_gettext('Book editor'),
        [Required(), Length(max=255)])
    publisher = StringField(lazy_gettext('Book publisher'),
        [Required(), Length(max=255)])
    style = SelectField(
        lazy_gettext('Select your css template !'),
        choices=[(template, template) for template in os.listdir(TEMPLATE_DIR) if os.path.isdir(os.path.join(TEMPLATE_DIR, template))]
        )
    language = SelectField(
        lazy_gettext('Select your language !'),
        choices=sorted([(short, name) for short, name in list(LANGUAGES.items())])
        )
    rights = TextField(lazy_gettext('Displayed Copyright'),
        [Length(max=255)])
    cover = FileField(lazy_gettext('Image File'),
        [FileAllowed(['jpg', 'png'], lazy_gettext('Images only!'))])


class AddPartForm(Form):
    title = TextField(lazy_gettext('Part title'),
        [Required(lazy_gettext('Title for that part is required.'))])
    content = TextAreaField(lazy_gettext('Content'))


class EditPartForm(Form):
    title = TextField(lazy_gettext('Part title'), [Required()])
    content = TextAreaField(lazy_gettext('Content'), [Required()])