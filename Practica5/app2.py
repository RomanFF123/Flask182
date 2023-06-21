from flask import Flask, render_template, request, redirect, url_for, flash #Importacion de librerias

from flask_mysqldb import MySQL





#iniciar servidor Flask

#configuracion de BD

app= Flask(__name__)

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

    return render_template('index.html')



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



@app.route('/eliminar')

def eliminar():

    return "Se elimino"





if __name__ == '__main__':

    app.run(port=5000, debug=True)