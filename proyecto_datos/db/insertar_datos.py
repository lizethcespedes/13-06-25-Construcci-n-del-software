from faker import Faker
import random
from db.conexion import obtener_conexion

def poblar_datos():
    fake = Faker()
    conn = obtener_conexion()
    cursor = conn.cursor()

    for _ in range(100):
        nombre = fake.name()
        edad = random.randint(20, 60)
        departamento = random.choice(['TI', 'Ventas', 'RRHH', 'Finanzas'])
        salario = round(random.uniform(1500, 5000), 2)

        cursor.execute('''
            INSERT INTO empleados (nombre, edad, departamento, salario)
            VALUES (?, ?, ?, ?)
        ''', (nombre, edad, departamento, salario))

    conn.commit()
    conn.close()
    print("Datos generados con Faker correctamente.")
