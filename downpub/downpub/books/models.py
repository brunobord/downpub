# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from downpub import db
from downpub.users.models import User
from downpub.books import constants as BOOK
from datetime import datetime


class Part(db.Model):

    __tablename__ = 'parts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    order = db.Column(db.Integer)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book = db.relationship('Book',
        backref=db.backref('parts', lazy='dynamic'))

    def __init__(self, title, content, order, book_id):
        """
        Init function of the Part model
        """
        self.title = title
        self.content = content
        self.order = order
        self.book_id = book_id

    def __repr__(self):
        """
        Prints the part
        """
        return '<Part %r>' % self.title


class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(255))
    cover = db.Column(db.String(255))
    displayed_name = db.Column(db.String(255))
    style = db.Column(db.String(255))
    language = db.Column(db.String(5))
    rights = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    editor = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    author = db.relationship('User',
        backref=db.backref('books', lazy='dynamic'))
    creation_date = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, title, subtitle, user_id, cover, style, language, rights,
        displayed_name, editor, publisher, creation_date, modified_at):
        """
        Init function of the Book model
        """
        self.title = title
        self.subtitle = subtitle
        self.user_id = user_id
        self.cover = cover
        self.displayed_name = displayed_name
        self.style = style
        self.language = language
        self.rights = rights
        self.editor = editor
        self.publisher = publisher

        if creation_date is None:
            creation_date = datetime.utcnow()
        self.creation_date = creation_date

        if modified_at is None:
            modified_at = datetime.utcnow()
        self.modified_at = modified_at

    def __repr__(self):
        """
        Prints the book
        """
        return '<Book %r, written by %r - %r>' % \
            (self.title, User.query.get(self.user_id).name, self.creation_date)