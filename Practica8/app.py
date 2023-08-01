from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración para la conexión a BD
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "dbflask"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# Declaración de rutas

@app.route('/')
def index():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM albums')
    consulta = curSelect.fetchall()
    return render_template('index.html', listAlbums=consulta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        v_titulo = request.form['txtTitulo']
        v_artista = request.form['txtArtista']
        v_anio = request.form['txtAnio']
        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO albums (titulo, artista, anio) VALUES (%s, %s, %s)', (v_titulo, v_artista, v_anio))
        mysql.connection.commit()
        flash('Album agregado correctamente :)')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM albums WHERE id = %s', (id,))
    consulId = curEditar.fetchone()
    return render_template('actualizar.html', album=consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        v_titulo = request.form['txtTitulo']
        v_artista = request.form['txtArtista']
        v_anio = request.form['txtAnio']
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE albums SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (v_titulo, v_artista, v_anio, id))
        mysql.connection.commit()
        flash('Album actualizado en BD :)')
    return redirect(url_for('index'))

@app.route('/borrar/<id>')
def borrar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM albums WHERE id = %s', (id,))
    consulId = curEditar.fetchone()
    return render_template('eliminar.html', album=consulId)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        curEli = mysql.connection.cursor()
        curEli.execute('DELETE FROM albums WHERE id=%s', (id,))
        mysql.connection.commit()
        flash('El álbum ha sido eliminado :)')
    return redirect(url_for('index'))

# Ejecución
if __name__ == '__main__':
    app.run(port=5000, debug=True)
