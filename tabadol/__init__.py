from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps, Map, icons
from flask_mail import Mail
from tabadol.config import Config
from sqlalchemy import event


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

GoogleMaps = GoogleMaps()


@event.listens_for(db.engine, "connect")
def load_spatialite(dbapi_conn, connection_record):
    # From https://geoalchemy-2.readthedocs.io/en/latest/spatialite_tutorial.html
    dbapi_conn.enable_load_extension(True)
    # point to /usr/local/lib/mod_spatialite.dylib
    dbapi_conn.load_extension('/usr/local/lib/mod_spatialite.dylib')
    dbapi_conn.execute('SELECT InitSpatialMetaData()')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    GoogleMaps.init_app(app)

    from tabadol.users.routes import users
    from tabadol.posts.routes import posts
    from tabadol.main.routes import main
    from tabadol.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # db.drop_all(app=app)
    db.engine.execute("SELECT InitSpatialMetaData();")
    db.create_all(app=app)

    return app
