from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LoginForm

#implementacion del formulario
@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            #Si las credenciales son correctas logear el usuario
            #con la funcion login_user()
            login_user(user,form.remember_me.data)
            #Next permite que el usuario siga a la pagina
            #que se le denego antes de logearse.
            next = request.args.get('next')
            
            if next is None or not next.startswith('/'):
                #si no hay una ruta en el next o no empieza con /
                #redirige el usuario a la pagina principal.
                next = url_for('main.index')
            return redirect(next)
        flash('Usuario o password invalido')
        return render_template('login.html',form=form)

    return render_template('login.html',form=form)
