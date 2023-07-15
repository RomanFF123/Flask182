
from flask import Flask, render_template, request, redirect, url_for, flash #importación de librerias
from flask_mysqldb import MySQL
#iniciazicón del servidor Flask

#Configuración para la BD
app= Flask(__name__)
app.config['MYSQL_HOST']= "localhost" #Aqui se especica el servicio/host/ip de un servidor
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="Fruteria"

app.secret_key='mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template ('repaso.html')


#Guardar Datos en la BD
@app.route('/guardar',methods=['POST']) 
def guardar():
    if request.method == 'POST':
        Fruta = request.form['txtFruta']
        Temporada = request.form['txtTemporada']
        Precio = request.form['txtPrecio']
        Stock = request.form['txtStock']
        # print(titulo,artista,anio)
        CS = mysql.connection.cursor() #Variable de tipo cursor que contiene las herramientas paara realizar los querys
        CS.execute("INSERT INTO inventario (frutas, temporada, precio, stock) VALUES (%s, %s, %s, %s)", (Fruta,Temporada,Precio, Stock))
        mysql.connection.commit()
    
    flash('Se ha hecho el registro Correctamente')    

    return redirect(url_for('index'))



#Actualizar Datos
@app.route('/actualizar/<id>',methods=['POST']) #Manera de definir las rutas
def actualizar(id):
    
    if request.method == 'POST':
        
        Fruta = request.form['txtFruta']
        Temporada = request.form['txtTemporada']
        Precio = request.form['txtPrecio']
        Stock = request.form['txtStock']
        
    curAct= mysql.connection.cursor()
    curAct.execute('update albums set Fruta=%s, Temporada= %s, Precio=%s, Stock=%s where id=%s', (Fruta, Temporada, Precio, Stock, id)) # %s
    mysql.connection.commit()
    
    flash('Album Actualizado Correctamente')    
    return redirect(url_for('index'))


#Rutas Eliminar
@app.route('/eliminar/<id>')
def eliminar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from inventario where id= %s',(id,))
    consultId= curEditar.fetchone()
    
    return render_template('editarfrutas.html',fruta= consultId)


@app.route()

#Ruta Editar
@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('select * from inventario where id= %s',(id,))
    consultId= curEditar.fetchone()
    
    return render_template('consulta.html',fruta= consultId)


if __name__ =='__main__':
    app.run(port= 5000, debug=True)