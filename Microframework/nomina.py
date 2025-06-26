from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sqlalchemy import create_engine, text

app = Flask(__name__)
engine = create_engine('sqlite:///data.db')

# Crear tabla si no existe
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            salario REAL
        )
    """))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    salario = float(request.form['salario'])

    # Crear DataFrame y guardar en DB
    df = pd.DataFrame([{'nombre': nombre, 'edad': edad, 'salario': salario}])
    df.to_sql('datos', con=engine, if_exists='append', index=False)

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    df = pd.read_sql('SELECT * FROM datos', con=engine)

    resumen = {
        'total_registros': len(df),
        'edad_promedio': round(df['edad'].mean(), 2),
        'salario_promedio': round(df['salario'].mean(), 2),
    }

    return render_template('dashboard.html', tabla=df.to_html(classes="table table-bordered"), resumen=resumen)

if __name__ == '__main__':
    app.run(debug=True)
