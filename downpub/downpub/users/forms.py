from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email
from flask.ext.babel import gettext, Babel


class LoginForm(Form):
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(Form):
    name = TextField('NickName', [Required()])
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message=gettext('Passwords must match'))
    ])
    accept_tos = BooleanField(gettext('I accept the TOS'), [Required()])
    recaptcha = RecaptchaField()