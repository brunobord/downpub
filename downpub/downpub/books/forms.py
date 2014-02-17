# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask.ext.wtf import Form
from wtforms import TextField, StringField, TextAreaField
from wtforms.validators import Required, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.babel import gettext


class AddForm(Form):
    title = StringField(gettext('Book title'),
        [Required(), Length(max=80)])

class AddCoverForm(Form):
    cover = FileField(gettext('Image File'),
        [FileAllowed(['jpg', 'jpeg', 'gif', 'png'], gettext('Images only!'))])


class EditForm(Form):
    title = TextField(gettext('Book title'),
        [Required(), Length(max=80)])
    cover = FileField(gettext('Image File'),
        [FileAllowed(['jpg', 'png'], gettext('Images only!'))])


class AddPartForm(Form):
    title = TextField(gettext('Part title'), [Required(gettext('Title for that part is required.'))])
    content = TextAreaField(gettext('Content'),
        default=gettext("#This is a default part title\n\nHere is the awesome content of that book's part."))
    order = TextField(gettext('Order'), [Required()])


class EditPartForm(Form):
    title = TextField(gettext('Part title'), [Required()])
    content = TextAreaField(gettext('Content'), [Required()])
    order = TextField(gettext('Order'), [Required()])