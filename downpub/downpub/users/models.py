# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from hashlib import md5

from downpub import db
from config import LANGUAGES
from downpub.users import constants as USER

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    locale = db.Column(db.Enum(list(LANGUAGES.keys())), name="locale", default='en', nullable=False)
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, name=None, email=None, password=None):
        """
        User model init function
        """
        self.name = name
        self.email = email
        self.password = password

    def getStatus(self):
        """
        Returns the status of the current user
        """
        return USER.STATUS[self.status]

    def getRole(self):
        """
        Returns the role of the current user
        """
        return USER.ROLE[self.role]

    def __repr__(self):
        """
        Returns the printable view of the current user (the name)
        """
        return '<User %r>' % (self.name)

    def avatar(self, size):
        """
        Returns the gratavar that match the user's email address
        """
        return 'http://www.gravatar.com/avatar/' + \
            md5(self.email.encode('utf-8')).hexdigest() + '?d=mm&s=' + str(size)
