# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import os.path

from flask.ext.wtf import Form
from wtforms import TextField, StringField, TextAreaField, SelectField
from wtforms.validators import Required, Length
from flask_wtf.file import FileField, FileAllowed
from flask.ext.babel import lazy_gettext

from config import TEMPLATE_DIR


class AddForm(Form):
    title = StringField(lazy_gettext('Book title'),
        [Required(), Length(max=80)])
    displayed_name = TextField(lazy_gettext('Displayed author name'),
        [Required(), Length(max=255)])
    style = SelectField(
        lazy_gettext('Select your css template !'),
        choices=[(template, template) for template in os.listdir(TEMPLATE_DIR) if os.path.isdir(os.path.join(TEMPLATE_DIR, template))]
        )


class AddCoverForm(Form):
    cover = FileField(lazy_gettext('Image File'),
        [FileAllowed(['jpg', 'jpeg', 'gif', 'png'],
        lazy_gettext('Images only!'))])


class EditForm(Form):
    title = TextField(lazy_gettext('Book title'),
        [Required(), Length(max=80)])

    displayed_name = TextField(lazy_gettext('Displayed author name'),
        [Required(), Length(max=255)])

    style = SelectField(
        lazy_gettext('Select your css template !'),
        choices=[(template, template) for template in os.listdir(TEMPLATE_DIR) if os.path.isdir(os.path.join(TEMPLATE_DIR, template))]
        )

    cover = FileField(lazy_gettext('Image File'),
        [FileAllowed(['jpg', 'png'], lazy_gettext('Images only!'))])


class AddPartForm(Form):
    title = TextField(lazy_gettext('Part title'),
        [Required(lazy_gettext('Title for that part is required.'))])
    content = TextAreaField(lazy_gettext('Content'))
    order = TextField(lazy_gettext('Order'), [Required()])


class EditPartForm(Form):
    title = TextField(lazy_gettext('Part title'), [Required()])
    content = TextAreaField(lazy_gettext('Content'), [Required()])
    order = TextField(lazy_gettext('Order'), [Required()])