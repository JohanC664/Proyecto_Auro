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
app.config['MYSQL_DB'] = 'flaskusuarios'
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