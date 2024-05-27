#Formulario para loggearse
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

#Clase que representa formulario para logearse.
#Se loggea un usuario que ya este registrado en la aplicacion
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

#Clase que representa el formulario de registro 
#para usuarios nuevos.
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64), Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,64),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                   'Username must have only letters,numbers, dots or'
                                   'underscore')])
    password = PasswordField('Pasword',validators=[DataRequired(),EqualTo('password2',message='Password must match')])
    password2 = PasswordField('Confirm Password',validators=[DataRequired()])
    submit =  SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
    