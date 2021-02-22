import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps, Map, icons
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# app.config.from_envvar('YOURAPPLICATION_SETTINGS')

# api key from Google API Console (https://console.cloud.google.com/apis/)

app.config['GOOGLEMAPS_KEY'] = os.environ.get('API_KEY')

# app.config.from_object('tabadol.default_settings')
# api_key = ' '  change this to your api key ""
# GoogleMaps(app, key=api_key)  set api_key 
# devices_data = {}  dict to store data of devices
# devices_location = {} # dict to store coordinates of devices
# use sqlalchemy or something to store things in database

GoogleMaps(app)
api_key = os.environ.get('API_KEY')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from tabadol import routes
