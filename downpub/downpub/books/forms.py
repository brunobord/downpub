from flask.ext.wtf import Form
from wtforms import TextField, StringField, TextAreaField
from wtforms.validators import Required, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.babel import gettext


class AddForm(Form):
    title = StringField(gettext('Book title'),
        [Required(), Length(max=80)])
    cover = FileField(gettext('Image File'),
        [FileAllowed(['jpg', 'png'], gettext('Images only!'))])


class EditForm(Form):
    title = TextField(gettext('Book title'),
        [Required(), Length(max=80)])
    cover = FileField(gettext('Image File'),
        [FileAllowed(['jpg', 'png'], gettext('Images only!'))])


class AddPartForm(Form):
    title = TextField(gettext('Part title'), [Required()])
    content = TextAreaField(gettext('Content'), [Required()])
    order = TextField(gettext('Order'), [Required()])


class EditPartForm(Form):
    title = TextField(gettext('Part title'), [Required()])
    content = TextAreaField(gettext('Content'), [Required()])
    order = TextField(gettext('Order'), [Required()])