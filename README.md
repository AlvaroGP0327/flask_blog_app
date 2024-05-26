Implementacion de autenticacion de usuario en Flask
Se requiere.
    1-Que el password en el objeto que representa al
    usuario este hasheado.
        from werkzeug.security import generate_password_hash,
        check_password_hash.
    
    2- Se requiere saber si un usuario esta logeado o no.
        pip install flask-login
        esta extension se usa para manejar el estado de un 
        usuario cuando esta navegando por nuestra aplicacion.
        Este estado se guarda en la user session.
        La clase usuario debe heredar de UserMixin
        Se debe inicializar flask-login en la aplication factory.

    3- se requiere generar y otorgar permisos.
    4- tener funcionalidades restringidas o protegidas.


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

