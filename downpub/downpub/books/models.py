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

    def __init__(self, title, content, order, book):
        self.title = title
        self.content = content
        self.order = order
        self.book = book

    def __repr__(self):
        return '<Post %r>' % self.title


class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    cover = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User',
        backref=db.backref('books', lazy='dynamic'))
    creation_date = db.Column(db.DateTime)

    def __init__(self, title, user_id, cover, creation_date):
        self.title = title
        self.user_id = user_id

        if cover is None:
            cover = "default"
        self.cover = cover

        if creation_date is None:
            creation_date = datetime.utcnow()
        self.creation_date = creation_date

    def __repr__(self):
        return '<Book %r, written by %r - %r>' % \
            (self.title, User.query.get(self.user_id).name, self.creation_date)