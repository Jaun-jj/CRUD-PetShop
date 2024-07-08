from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

#csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña inválida...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


#@app.route('/home')
#def home():
 #   return render_template('home.html')


@app.route('/protected')
@login_required
def protected():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM user")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('protected.html', data=insertObject)
    
@app.route('/home')
def home():
    cursor = db.connection.cursor()
    cursor.execute("SELECT id, nombre, correo, pregunta FROM contacto")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('home.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    fullname = request.form['name']
    password = request.form['password']

    if username and fullname and password:
        cursor = db.connection.cursor()
        sql = "INSERT INTO user (username, fullname, password) VALUES (%s, %s, %s)"
        data = (username, fullname, password)
        cursor.execute(sql, data)
        db.connection.commit()
    return redirect(url_for('protected'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.connection.cursor()
    sql = "DELETE FROM user WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('protected'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    username = request.form['username']
    fullname = request.form['name']
    password = request.form['password']

    if username and fullname and password:
        cursor = db.connection.cursor()
        sql = "UPDATE user SET username = %s, fullname = %s, password = %s WHERE id = %s"
        data = (username, fullname, password, id)
        cursor.execute(sql, data)
        db.connection.commit()
    return redirect(url_for('protected'))


#Del Front de PET SHOP

@app.route('/front')
def front():

    return render_template('Front/contacto.html')


@app.route('/addcontacto', methods=['POST'])
def addContacto():
    nombre = request.form['Nombre']
    apellido = request.form['Apellido']
    telefono = request.form['Telefono']
    correo = request.form['email']
    #mascota = request.form['selmascota']
    pregunta = request.form['Consulta']
    foto = request.form['file']
    #correoNews = request.form['Correo2']
    #selectionNews = request.form['check1']

    
    cursor = db.connection.cursor()
    sql = "INSERT INTO contacto (nombre, apellido, telefono, correo, pregunta, foto ) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (nombre, apellido, telefono, correo, pregunta, foto)
    cursor.execute(sql, data)
    db.connection.commit()
    return render_template('Front/contacto.html')

@app.route('/delete2/<string:id>')
def delete2(id):
    cursor = db.connection.cursor()
    sql = "DELETE FROM contacto WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('home'))

@app.route('/edit2/<string:id>', methods=['POST'])
def edit2(id):
    nombre = request.form['nombre']
    correo = request.form['email']
    pregunta = request.form['pregunta']

    if nombre and correo and pregunta:
        cursor = db.connection.cursor()
        sql = "UPDATE contacto SET nombre = %s, correo = %s, pregunta = %s WHERE id = %s"
        data = (nombre, correo, pregunta, id)
        cursor.execute(sql, data)
        db.connection.commit()
    return redirect(url_for('home'))



def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
