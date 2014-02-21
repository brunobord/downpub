# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.babel import gettext, Babel

from downpub import downpub, db, babel
from downpub.users.forms import RegisterForm, LoginForm, LocaleForm
from downpub.users.models import User
from downpub.users.decorators import requires_login
from config import LANGUAGES

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
        g.user_id = session['user_id']
        g.locale = g.user.locale


@mod.route('/me/', methods=['GET', 'POST'])
@requires_login
def home():
    """
    user's profile view page
    """

    site_title = gettext('Profile page')
    form = LocaleForm(request.form)

    # form shows the current locale of the user
    if not form.validate_on_submit():
        user = User.query.get(g.user_id)
        form.locale.data = user.locale

    # if the user changed his/her locale setting, we save it
    if form.validate_on_submit():
        # we get the user record
        user = User.query.get(g.user_id)
        # we set the new value for locale
        user.locale = form.locale.data
        # we commit
        db.session.commit()
        flash(gettext(
            "Locale's been changed to %(locale)s", locale=user.locale
        ))
        return render_template("users/profile.html",
            form=form, user=g.user, site_title=site_title)

    return render_template("users/profile.html",
        form=form, user=g.user, site_title=site_title)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Login form
    """
    site_title = gettext('Login page')

    form = LoginForm(request.form)

    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # we first test if the user was not found
        if user is None:
            flash(gettext('Unknown user !'), 'error-message')
            return render_template("users/login.html", form=form, user=g.user, site_title=site_title)
        # then we check the password
        elif check_password_hash(user.password, form.password.data):
            # the session can't be modified as it's signed,
            # it's a safe place to store the user id
            session['user_id'] = user.id
            flash(gettext("You're logged in, %(name)s", name=user.name))
            return redirect(request.args.get("next")
                or url_for('users.home'))
        else:
            # if we get here, that means the user is in the db, but the entered password was wrong
            flash(gettext('Wrong password'), 'error-message')
            return render_template("users/login.html", form=form, user=g.user, site_title=site_title)
    return render_template("users/login.html", form=form, user=g.user, site_title=site_title)


@mod.route("/logout")
@requires_login
def logout():
    """
    Log the current user out and redirect on the index
    """
    session.clear()
    g.user = None
    user = None
    flash(gettext("You've been logged out."))
    return redirect(url_for('index'))


@mod.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Registration Form
    """

    site_title = gettext('Register page')

    form = RegisterForm(request.form)

    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        user = User(name=form.name.data, email=form.email.data,
        password=generate_password_hash(form.password.data))

        # Insert the record in our database and commit it
        db.session.add(user)
        db.session.commit()

        # Log the user in, as he now has an id
        session['user_id'] = user.id

        # flash will display a message to the user
        flash(gettext('Thanks for registering %(name)s', name=user.name))
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('users.home'))

    return render_template("users/register.html", form=form, user=g.user, site_title=site_title)
