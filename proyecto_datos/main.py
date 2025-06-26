from db.conexion import crear_tabla
from db.insertar_datos import poblar_datos
from procesamiento.analisis import leer_datos, analizar_datos
from procesamiento.reportes import exportar_reportes
from visuales.graficos import generar_grafico

if __name__ == '__main__':
    crear_tabla()
    poblar_datos()
    df = leer_datos()
    resumen, top_5, promedio_general, edad_prom = analizar_datos(df)
    exportar_reportes(df, resumen, top_5, promedio_general, edad_prom)
    generar_grafico(resumen)
    print("Todo el proceso ha terminado.")
