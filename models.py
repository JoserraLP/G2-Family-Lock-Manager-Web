from flask_login import UserMixin
from . import db

import datetime

class User(UserMixin, db.Model):
    ''' Class representing a web server user

    Attributes
    ----------
    id : int 
        User identificator
    email : str 
        User email
    password : str
        User password
    name : str 
        User name
    email_confirmed_at : date
        Email confirmation date
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(20))
    name = db.Column(db.String(100))
    
    # Necessary to Flask user
    email_confirmed_at = db.Column(db.DateTime())