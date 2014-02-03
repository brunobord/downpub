from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, StringField, TextAreaField, FileField
from wtforms.validators import Required, Length, EqualTo, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class AddForm(Form):
  title = StringField('Book title', [Required(), Length(max=80)])
  cover = FileField('Image File', 
    [FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

class EditForm(Form):
  title = TextField('Book title', [Required(), Length(max=80)])
  cover = FileField(u'Image File', 
    [FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

class AddPartForm(Form):
  title = TextField('Part title', [Required()])
  content = TextAreaField('Content', [Required()])
  order = TextField('Order', [Required()])

class EditPartForm(Form):
  title = TextField('Part title', [Required()])
  content = TextAreaField('Content', [Required()])
  order = TextField('Order', [Required()])