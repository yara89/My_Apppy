import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # api key from Google API Console (https://console.cloud.google.com/apis/)

    GOOGLEMAPS_KEY = os.environ.get('API_KEY')

    # app.config.from_object('tabadol.default_settings')
    # api_key = ' '  change this to your api key " "
    # GoogleMaps(app, key=api_key)  set api_key map_key=
    # devices_data = {}  dict to store data of devices
    # devices_location = {} # dict to store coordinates of devices
    # use sqlalchemy or something to store things in database

    # Mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
