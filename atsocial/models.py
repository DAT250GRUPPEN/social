from atsocial import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin






@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True) #Unique id to each user 
    #profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    first_name = db.Column(db.String(20),nullable=False,index=True)
    last_name = db.Column(db.String(20),nullable=False,index=True)
    email = db.Column(db.String(64), unique=True, index=True) 
    #gender = db.Column(db.)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # This connects Posts to a User Author.
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, first_name,last_name,email, username, password): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
      


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"UserName: {self.username}"

class Post(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, text, user_id):
        self.text = text
        self.user_id =user_id


    def __repr__(self):
        return f"Post Id: {self.id} --- Date: {self.date} --- Title: {self.title}"


