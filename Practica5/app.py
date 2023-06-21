
from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL
#iniciazicón del servidor Flask

#Configuración para la BD
app= Flask(__name__)
app.config['MYSQL_HOST']= "localhost" #Aqui se especica el servicio/host/ip de un servidor
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysecretkey'
mysql = MySQL(app)

#Declaración de Ruta 

#Ruta index http://localhost:5000
#La ruta se compone del nombre de la ruta y su función
@app.route('/')
def index():
    return render_template ('index.html') #Render template genera la vista y la podamos ver

@app.route('/guardar',methods=['POST']) #Manera de definir las rutas
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        anio = request.form['txtAnio']
        # print(titulo,artista,anio)
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO albums (titulo, artista, anio) VALUES (%s, %s, %s)", (titulo, artista, anio))
        mysql.connection.commit()
    
    flash('Album Agregado Correctamente')    

    return redirect(url_for('index'))
    

@app.route('/eliminar')
def eliminar():
    return "Se elemino de la BD"


# Lineas que ejecutan el servidor
if __name__ =='__main__':
    app.run(port= 5000, debug=True)
    
    