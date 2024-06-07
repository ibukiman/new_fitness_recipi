from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin

from apps.recipiapp import db

class User(db.Model,UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),index=True,unique=True,nullable=False)
    password_hash = db.Column(db.String,nullable=False)
    creat_at = db.Column(db.DateTime,default=datetime.now)

    @property
    def password(self):
        raise AttributeError('password is not a readabe')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def is_duplicate_username(self):
        return User.query.filter_by(username=self.username).first() is not None
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    
# from apps.mainapp import models

# class LikeRecipi(db.Model,table=True):
#     __tablename__='likerecipes'
#     table_args = {'extend_existing': True}
#     user_id = db.Column(db.Integer,primary_key=True)
#     recipi_id = db.Column(db.Integer,db.ForeignKey(models.UserRecipi.id),nullable=False)
#     like_now = db.Column(db.Integer)

# class aieuo(db.Model):
#     __tablename__="aiueo_table"
#     id = db.Column(db.Integer,primary_key=True)
#     aiueo = db.Column(db.String(30))