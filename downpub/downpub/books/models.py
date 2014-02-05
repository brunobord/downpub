from downpub import db
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
        backref=db.backref('part', lazy='dynamic'))

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

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    creation_date = db.Column(db.DateTime)

    def __init__(self, title, user, creation_date=None):
        self.title = title
        self.user = user
        if creation_date is None:
            creation_date = datetime.utcnow()
        self.creation_date = creation_date

    def __repr__(self):
        return '<Book %r, written by %r - %r>' % (self.title, self.author, self.creation_date)