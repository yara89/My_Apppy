from tabaodol import db, bcrypt
from tabadol.models import User, UserTypes, OfferType, Post


#db.drop_all()
db.engine.execute("SELECT InitSpatialMetaData();")

db.create_all()

# insert myself as admin user
hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
admin = User(username='YarZ', email='YARA3001@gmail.com',
             password=hashed_password, user_type=UserTypes.Admin)
db.session.add(admin)

# insert OFFER types
give = OfferType(number=1, name='give')
need = OfferType(number=2, name='need')

db.session.add(give)
db.session.add(need)

db.session.commit()
