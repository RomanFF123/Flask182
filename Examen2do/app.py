# https://github.com/RomanFF123/Flask182

from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL
#iniciazicón del servidor Flask

#Configuración para la BD
app= Flask(__name__)
app.config['MYSQL_HOST']= "localhost" #Aqui se especica el servicio/host/ip de un servidor
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="DB_Floreria"

app.secret_key='mysecretkey'
mysql = MySQL(app)



@app.route('/')
def index():
    cursorSelect= mysql.connection.cursor()
    cursorSelect.execute("SELECT * FROM tbFlores;")
    consulta= cursorSelect.fetchall()
    #print(consulta)
    return render_template('index.html',listFlores= consulta)



#Guardar Datos en la BD
@app.route('/guardar',methods=['POST']) 
def guardar():
    if request.method == 'POST':
        nombre = request.form['txtnombre']
        cantidad = request.form['txtcantidad']
        precio = request.form['txtPrecio']
        # print(titulo,artista,anio)
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO tbFlores (nombre, cantidad, precio) VALUES (%s, %s, %s)", (nombre, cantidad, precio))
        mysql.connection.commit()
    
    flash('Se ha hecho el registro Correctamente')    

    return redirect(url_for('index'))



#Ruta Eliminar
@app.route('/eliminar/<id>')
def eliminar(id):
    curEliminar = mysql.connection.cursor()
    curEliminar.execute('DELETE FROM tbFlores WHERE id = %s', (id))
    mysql.connection.commit()
    
    flash('El Registro se ha Eliminado Correctamente')
    return redirect(url_for('index.html'))

@app.route('/tabla')
def consultar():
    return render_template ('consulta.html') 


if __name__ =='__main__':
    app.run(port= 5000, debug=True)