from flask import Flask
from .models import db  # Importuj db iz models.py
from .routes import main
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Inicijalizuj db sa aplikacijom
    migrate = Migrate(app,db)
    app.register_blueprint(main)

    return app


