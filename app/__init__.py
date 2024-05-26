#Application Factory.
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()
#configuraciones usuario logeado 
login_manager = LoginManager()
#Vista que maneja el login dentro de auth
#se redirecciona aqui a la pagina de login
login_manager.login_view = 'auth.login'


def create_app(config_name:str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)    
    #Importar e inicializar las Blueprints
    #Autenticacion
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app

