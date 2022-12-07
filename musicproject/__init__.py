import os

from flask import Flask, redirect
from musicproject.database import init_db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app with the database
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'musicMatch.db'),
    )

    db = SQLAlchemy(app)
    db.app = app

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # redirects to home page
    @app.route('/')
    def index():
        return redirect("/home")

    # run the code on our auth and application pages
    from . import auth, application
    app.register_blueprint(auth.bp)
    app.register_blueprint(application.bp)

    db.init_app(app)

    init_db()

    return app