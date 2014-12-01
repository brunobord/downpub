# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, SelectField
from wtforms.validators import Required, EqualTo, Email, ValidationError
from flask.ext.babel import lazy_gettext, Babel

from downpub import db
from config import LANGUAGES
from downpub.users.models import User


def unique_email_check(form, field):
    """
    Custom validator that checks if an given email is already used by someone
    """
    existing_email = User.query.filter_by(email=field.data).all()

    if existing_email:
        raise ValidationError(lazy_gettext('Someone already uses this email address.'))


class LocaleForm(Form):
    """
    Form to change user's locale
    """
    locale = SelectField(
        lazy_gettext('Select your new default locale !'),
        choices=[(short, language) for short, language in list(LANGUAGES.items())]
    )


class LoginForm(Form):
    """
    Login form
    """
    email = TextField(lazy_gettext('Email address'),
        [Required(lazy_gettext('An email is required.')),
        Email(lazy_gettext("It's not a proper email adress."))])
    password = PasswordField(lazy_gettext('Password'),
        [Required(lazy_gettext('Enter a password.'))])


class RegisterForm(Form):
    """
    Registration Form
    """
    name = TextField(lazy_gettext('NickName'), [Required(lazy_gettext('Enter a nickname.'))])
    email = TextField(lazy_gettext('Email address'),
        [Required(lazy_gettext('An email is required.')),
        Email(lazy_gettext("It's not a proper email adress.")),
        unique_email_check])
    password = PasswordField(lazy_gettext('Password'),
        [Required(lazy_gettext('Enter a password.'))])
    confirm = PasswordField(lazy_gettext('Repeat Password'),
    [
        Required(lazy_gettext('Enter the same password.')),
        EqualTo('password', message=lazy_gettext('Passwords must match'))
    ])
    accept_tos = BooleanField(lazy_gettext('I promise to behave.'),
        [Required(lazy_gettext("Well, I can't accept your registration if you don't check this one."))])
    recaptcha = RecaptchaField()

