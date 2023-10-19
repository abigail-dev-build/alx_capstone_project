from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
# from sqlalchemy_imageattach.entity import Image, image_attachment

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    category = db.Column(db.String(50))
    author = db.Column(db.String(150))
    # image = image_attachment('UserPicture')
    content = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
# class PostPicture(db.Model, Image):
#     '''Post's thumbmail picture.'''
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
#     picture = db.relationship('Post')
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    notes = db.relationship('Post')
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=False)
    email = db.Column(db.String(150), unique=False)
    comment = db.Column(db.String(150), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post')
    status = db.Column(db.Boolean, default=False)