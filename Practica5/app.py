
from flask import Flask #importación de libreria

#iniciazicón del servidor Flask

#Configuración para la BD
app= Flask(__name__)
app.config['MYSQL_HOST']= "localhost" #Aqui se especica el servicio/host/ip de un servidor
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbflask"


#Declaración de Ruta 

#Ruta index http://localhost:5000
#La ruta se compone del nombre de la ruta y su función
@app.route('/')
def index():
    return "Hola Yorch Godina Mejorado"

@app.route('/guardar')
def guardar():
    return "Se guardo el registro en la BD correctamente"

@app.route('/eliminar')
def eliminar():
    return "Se elemino de la BD"


# Lineas que ejecutan el servidor
if __name__ =='__main__':
    app.run(port= 5000, debug=True)
    
    