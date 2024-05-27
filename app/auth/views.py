from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm

#implementacion del formulario inicio de sesion
@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #si los datos en el formulario son validos
        #buscar si el email proporcionado existe
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            #Si el usuario existe y las credenciales son correctas logear el usuario
            #con la funcion login_user()
            #login_user escribe los datos del usuario en la session
            login_user(user,form.remember_me.data)
            #Next permite que el usuario siga a la pagina
            #que se le denego antes de logearse.
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                #si no hay una ruta en el next o no empieza con /
                #asignar a next la redireccion a main.index
                next = url_for('main.index')
            return redirect(next)
        #Si los datos del formulario son validos.Pero no coinciden
        #con ningun usuario en la db flash()
        #y retornar el formulario vacio
        flash('Usuario o password invalido')
        return render_template('login.html',form=form)

    return render_template('login.html',form=form)

#Ruta para deslogear un usuario y limpiar la sesion
@auth.route('/logout')
@login_required
def logout():
    flash('Se ha deslogeado con exito')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',form=form)