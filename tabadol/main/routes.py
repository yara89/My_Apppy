from flask import render_template, request, Blueprint
from tabadol.models import Post
from flask_googlemaps import GoogleMaps, Map, icons

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(
      Post.date_posted.desc()).paginate(page=page, per_page=5)
  return render_template('home.html', posts=posts)


@main.route("/about")
def about():
  return render_template('about.html', title='About')


@main.route("/maps", methods=['GET', 'POST'])
def maps():
  local = Local.query.all()
  print(local)
  #  gmap = Map(
  #     identifier="gmap",
  #      varname="gmap",
  #     lat=37.4419,
  #     lng=-122.1419,
  #     markers=[{'lat': 52.4845, 'lng': 13.4344},
  #              {'lat': 52.5042, 'lng': 13.4536},
  #              {'lat': 52.5178, 'lng': 13.3810}],)

  # icons.dots.green:   [(, ), (, )]
  # icons.dots.blue: [(, , "Hello World")], add also...gmap=gmap
  return render_template("maps.html",  title='Map of maps', local=local)
