import pandas as pd
from db.conexion import obtener_conexion

def leer_datos():
    conn = obtener_conexion()
    df = pd.read_sql_query("SELECT * FROM empleados", conn)
    conn.close()
    return df

def analizar_datos(df):
    print("\nResumen por departamento:")
    resumen = df.groupby('departamento')['salario'].agg(['count', 'mean', 'max', 'min'])
    print(resumen)

    #Top 5 empleados mejor pagados
    print("\nTop 5 empleados mejor pagados:")
    top_5 = df.sort_values(by='salario', ascending=False).head(5)
    print(top_5[['nombre', 'departamento', 'salario']])

    #Salario promedio general
    promedio_general = df['salario'].mean()
    print(f"\nSalario promedio general: ${promedio_general:.2f}")

    #Edad promedio por departamento
    print("\nEdad promedio por departamento:")
    edad_prom = df.groupby('departamento')['edad'].mean().round(2)
    print(edad_prom)
    return resumen, top_5, promedio_general, edad_prom
