import sqlite3

def obtener_conexion():
    return sqlite3.connect('datos.db')

def crear_tabla():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            departamento TEXT,
            salario REAL
        )
    ''')
    conn.commit()
    conn.close()
