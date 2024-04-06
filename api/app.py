from flask import Flask,jsonify
from config import Config
import pyodbc

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = pyodbc.connect(app.config['DATABASE_CONNECTION_STRING'])
    return conn

@app.route('/vista-detalles-empleados', methods=['GET'])
def vista_detalles_empleados():
    """
    Esta ruta consulta la vista 'VistaDetallesEmpleados' y devuelve los resultados en formato JSON.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VistaDetallesEmpleados")

    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
