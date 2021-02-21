from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# app.config.from_object('tabadol.default_settings')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
# api_key = ' '  change this to your api key
#  api key from Google API Console (https://console.cloud.google.com/apis/)
# GoogleMaps(app, key=api_key)  set api_key
# devices_data = {}  dict to store data of devices
# devices_location = {} # dict to store coordinates of devices
# use sqlalchemy or something to store things in database

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from tabadol import routes
