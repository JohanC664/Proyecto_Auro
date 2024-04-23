from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'mysecretekey'

users = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2',
}

# mysql connection configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'auro'
mysql = MySQL(app)

# --------------------------------------------------#
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM personas')
    data = cur.fetchall()
    return render_template('index.html', usuarios=data)

#----------------------mod registrate--------------------------------#

@app.route('/mod_registrate.html')
def mod_registrate():
    return render_template('mod_registrate.html')

#--------------- registrar como aprendiz ---------------#

@app.route ('/registro_aprendiz.html')
def registro_aprendiz ():
    return render_template('registro_aprendiz.html')

@app.route ('/add_aprendiz', methods = ['POST'])
def registro_un_aprendiz ():
    if request.method == 'POST':
        num_documento = request.form ['num_documento']
        nombre_aprendiz = request.form ['nombre_aprendiz']
        usuario_aprendiz = request.form ['usuario_aprendiz']
        carrera_aprendiz = request.form ['carrera_aprendiz']
        telefono_aprendiz = request.form ['telefono_aprendiz']
        correo_aprendiz = request.form ['correo_aprendiz']
        contrasena_aprendiz = request.form ['contrasena_aprendiz']
        
        
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO aprendices (num_documento, nombre_aprendiz, usuario_aprendiz, carrera_aprendiz, telefono_aprendiz, correo_aprendiz, contrasena_aprendiz) VALUES (%s, %s, %s, %s, %s, %s, %s )',
                    (num_documento,nombre_aprendiz,usuario_aprendiz,carrera_aprendiz, telefono_aprendiz, correo_aprendiz, contrasena_aprendiz))
        
        mysql.connection.commit()
        
        return 'received'


#----------- Mod aprendiz --------------#

@app.route ('/mod_aprendiz.html')
def mod_aprendiz ():
    return render_template ('mod_aprendiz.html')

#----------- mod portafoleo -----------#

@app.route ('/mod_portafoleo.html')
def mod_aportafoleo ():
    return render_template ('mod_portafoleo.html')

if __name__ == '__main__':
    app.run(debug=True)