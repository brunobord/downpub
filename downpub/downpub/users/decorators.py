# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from functools import wraps
from flask.ext.babel import gettext
from flask import g, flash, redirect, url_for, request


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(gettext('You need to be signed in for this page.'))
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function