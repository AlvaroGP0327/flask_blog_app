Implementacion de autenticacion de usuario en Flask
Se requiere.
    1-Que el password en el objeto que representa al
    usuario este hasheado.
    se implementa en la clase User
        from werkzeug.security import generate_password_hash,
        check_password_hash.
    
    2- Se requiere saber si un usuario esta logeado o no.
        pip install flask-login
        esta extension se usa para manejar el estado de un 
        usuario cuando esta navegando por nuestra aplicacion.
        Este estado se guarda en la user session.
        La clase usuario debe heredar de UserMixin
        Se debe inicializar flask-login en la aplication factory.
        from flask_login import LoginManager
        login_manager= LoginManager()
        login_manager.login_view = 'endpointdellogin'
        login_manager.init(app)

    3- En el archivo models importar la instancia login_manager
        y crear la funcion 
        @login_manager.user_loader
        load_user(user_id).
    4- Proteger la ruta con @login_required

**Extensiones
    -Flask-Login:Proceso de suministrar credenciales por
    parte del usuario, y la aplicacion las verifica para
    permitir el acceso a funcionalidades restringidas.
    -Werkzeug: Hashear el password y verificarlo.
    -itsdangerous: generar y verificar tokens.

**Paquetes de proposito general
    -Flask-Mail.
    -Flask-Bootstrap
    -Flask-wtf.

