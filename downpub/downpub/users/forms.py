from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email
from flask.ext.babel import gettext, Babel


class LoginForm(Form):
    email = TextField(gettext('Email address'), [Required(gettext('An email is required.')),
        Email(gettext("It's not a proper email adress."))])
    password = PasswordField(gettext('Password'), [Required(gettext('Enter a password.'))])


class RegisterForm(Form):
    name = TextField(gettext('NickName'), [Required(gettext('Enter a nickname.'))])
    email = TextField(gettext('Email address'), [Required(gettext('An email is required.')),
        Email(gettext("It's not a proper email adress."))])
    password = PasswordField(gettext('Password'), [Required(gettext('Enter a password.'))])
    confirm = PasswordField(gettext('Repeat Password)'),
    [
        Required(gettext('Enter the same password.')),
        EqualTo('password', message=gettext('Passwords must match'))
    ])
    accept_tos = BooleanField(gettext('I promise to behave.'),
        [Required(gettext("Well, I can't accept your registration if you don't check this one."))])
    recaptcha = RecaptchaField()