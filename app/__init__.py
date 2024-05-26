#Application Factory.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()

def create_app(config_name:str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    
    #Importar e inicializar las Blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app

