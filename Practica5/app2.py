from flask import Flask, render_template, request, redirect, url_for, flash #Importacion de librerias
from flask_mysqldb import MySQL


#iniciar servidor Flask
#configuracion de BD
app= Flask(_name_)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWWORD']=""
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysecretkey'

mysql = MySQL(app)

#Declaracion de la ruta
#Ruta index
#La ruta se compone de la ruta y su funcion
@app.route('/')
def index():
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("Select * from albums")
    consulta= cursorSelect.fetchall()
    #print(consulta)
    return render_template('index.html', listAlbums= consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        #print()
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO albums (titulo, artista, anio) VALUES (%s, %s, %s)", (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
    flash('Album Agregado Correctamente')    
    return redirect(url_for('index'))


@app.route('/editar')
def editar():
    return render_template('editarAlbum.html')


@app.route('/eliminar')
def eliminar():
    return "Se elimino"


if _name_ == '_main_':
    app.run(port=5000, debug=True)