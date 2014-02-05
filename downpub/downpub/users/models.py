from hashlib import md5

from downpub import db
from downpub.users import constants as USER

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + \
            md5(self.email.encode('utf-8')).hexdigest() + '?d=mm&s=' + str(size)
