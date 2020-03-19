from flask import Flask, url_for, redirect
from flask_mongoengine import MongoEngine
from config import Config

# from flask_login import LoginManager

db = MongoEngine()


# login_manager = LoginManager(app)

def create_app():
    app = Flask(__name__)

    # This line just for loaclhost

    db.init_app(app)
    app.config.from_object(Config)

    from user.view import user_page
    app.register_blueprint(user_page, url_prefix="/user")

    from party.views import party_page
    app.register_blueprint(party_page, url_prefix="/party")

    @app.route('/')
    def home():
        return redirect(url_for('party_page.explore'))

    return app
