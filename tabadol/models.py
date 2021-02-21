import enum
from datetime import datetime
from tabadol import db, login_manager
from flask_login import UserMixin
from sqlalchemy import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserTypes(enum.Enum):
    Admin = 1
    Regular = 2


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.Enum(UserTypes),
                          nullable=False, default=UserTypes.Regular)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # Relationship between offers and the users
    user_offers = db.relationship(
        'Post', back_populates='user', order_by="Post.id", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', type:{self.user_type})"


class Post(db.Model):
    __tablename__ = 'user_offers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship("User", back_populates="user_offers")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
