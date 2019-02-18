from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__ = "posts"
    id  = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String)
    time = db.Column(db.String)
    image = db.Column(db.String)
    # comments = db.relationship("Comment",backref = "post", lazy = "dynamic")
    # def get_post_comments(self):
    #     return Comment.query.filter_by(post_id = self.id)

    def save_post(self):
        db.session.add(self)
        db.session.commit()

class Subscriber(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()
