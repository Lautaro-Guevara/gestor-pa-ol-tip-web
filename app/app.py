from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tipsadb'
app.config['MYSQL_DB'] = 'pañol_db'

mysql = MySQL(app)

def obtener_conexion():
    return MySQLdb.connect(
        user='root',
        passwd='tipsadb',
        host='localhost',
        db='pañol_db'
    )

print(obtener_conexion())

@app.route('/')
def index():
    return render_template('index.html')



@app.route("/ejemplo")
def ejemplo():
    return render_template("ejemplo.html")

if __name__ == '__main__':
    app.run(debug=True)
