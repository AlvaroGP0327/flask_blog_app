#Formulario para loggearse
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

#Clase que representa formulario para logearse.
#Se loggea un usuario que ya este registrado en la aplicacion
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired(),])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

#Clase que representa el formulario de registro 
#para usuarios nuevos.
class RegistrationForm():
    pass 