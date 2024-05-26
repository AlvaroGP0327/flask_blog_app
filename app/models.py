#Modelos para la base de datos.
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    users = db.relationship('User',backref='role')

class User(UserMixin,db.Model):
    #Instanciar con el password hasheado
    #Encapsular el atributo password_hash
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #Atributo password es de solo lectura
    #encapsular password_hash
    @property
    #getter
    def password(self):
        raise AttributeError('No se puede leer el password') 
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
#Funcion que maneja la carga de usuarios desde la base de datos
#dado una identificacion.
#Trae la informacion del usuario logeado
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))