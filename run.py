from tabadol import create_app


# with app.app_context():
#   init_db()

app = create_app()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
