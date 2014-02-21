# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, SelectField
from wtforms.validators import Required, EqualTo, Email, ValidationError
from flask.ext.babel import gettext, Babel

from downpub import db
from config import LANGUAGES
from downpub.users.models import User


def unique_email_check(form, field):
    """
    Custom validator that checks if an given email is already used by someone
    """
    existing_email = User.query.filter_by(email=field.data).all()

    if existing_email:
        raise ValidationError(gettext('Someone already uses this email adress.'))


class LocaleForm(Form):
    """
    Form to change user's locale
    """
    locale = SelectField(
        gettext('Select your new default locale !'),
        choices=[(languague, languague) for languague in LANGUAGES]
        )


class LoginForm(Form):
    """
    Login form
    """
    email = TextField(gettext('Email address'), [Required(gettext('An email is required.')),
        Email(gettext("It's not a proper email adress."))])
    password = PasswordField(gettext('Password'), [Required(gettext('Enter a password.'))])


class RegisterForm(Form):
    """
    Registration Form
    """
    name = TextField(gettext('NickName'), [Required(gettext('Enter a nickname.'))])
    email = TextField(gettext('Email address'), [Required(gettext('An email is required.')),
        Email(gettext("It's not a proper email adress.")),
        unique_email_check])
    password = PasswordField(gettext('Password'), [Required(gettext('Enter a password.'))])
    confirm = PasswordField(gettext('Repeat Password'),
    [
        Required(gettext('Enter the same password.')),
        EqualTo('password', message=gettext('Passwords must match'))
    ])
    accept_tos = BooleanField(gettext('I promise to behave.'),
        [Required(gettext("Well, I can't accept your registration if you don't check this one."))])
    recaptcha = RecaptchaField()

