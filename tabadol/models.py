import enum
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from tabadol import db, login_manager
from flask_login import UserMixin
from sqlalchemy import func
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKTElement
import json


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserTypes(enum.Enum):
    Admin = 1
    Regular = 2


class SpatialConstants:
    # SRID stands for Spatial Reference ID, some explanation of why we need one here:
    # https://www.gaia-gis.it/gaia-sins/spatialite-cookbook/html/srid.html
    SRID = 4326


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

    # Relationship between offers and users
    user_offers = db.relationship(
        'Post', back_populates='user', order_by="Post.id", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', type:{self.user_type})"


class OfferType(db.Model):
    __tablename__ = 'offer_types'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref='offer_type', lazy=True)

    def __repr__(self):
        return f"offertype('{self.number}', '{self.name}')"


class Post(db.Model):
    __tablename__ = 'user_offersv2'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    location = db.Column(
        Geometry("POINT", srid=4326, dimension=2, management=True))
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    offer_type_id = db.Column(db.Integer, db.ForeignKey(
        'offer_types.id'), nullable=False)
    user = db.relationship("User", back_populates="user_offers")

    def get_post_location_lat(self):
        point = to_shape(self.location)
        return point.x

    def get_post_location_lng(self):
        point = to_shape(self.location)
        return point.y

    def __repr__(self):
        return f"Post('{self.title}', '{self.location}', '{self.date_posted}')"

    @staticmethod
    def point_representation(lat, lng):
        point = 'POINT(%s %s)' % (lat, lng)
        wkb_element = WKTElement(point, srid=4326)
        return wkb_element

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user.username,
            'title': self.title,
            'address': self.address,
            'location': {
                'lat': self.get_offer_location_lat(),
                'lng': self.get_offer_location_lng(),
            },
            'content': self.content,
            'offer_type': self.offer_type.name
        }

    @staticmethod
    def get_offers_within_radius(lat, lng, radius):
        # Return all posts within a given radius (in meters)
        return Post.query.filter(
            func.PtDistWithin(
                Post.location,
                func.MakePoint(lat, lng, 4326),
                radius)
        ).all()


class Local(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Local('{self.name}', '{self.latitude}' {self.longitude}')"
