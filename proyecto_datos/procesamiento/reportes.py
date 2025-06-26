def exportar_reportes(df, resumen, top_5, promedio_general, edad_prom):
    df.to_csv('reporte_empleados.csv', index=False)
    df.to_excel('reporte_empleados.xlsx', index=False)

    with open('reporte_empleados.txt', 'w') as f:
        f.write("Datos completos:\n")
        f.write(df.to_string())
        f.write('\n\nResumen por Departamento:\n')
        f.write(resumen.to_string())
        f.write('\n\nTop 5 Empleados Mejor Pagados:\n')
        f.write(top_5.to_string())
        f.write(f'\n\nSalario Promedio General: ${promedio_general:.2f}\n')
        f.write('\n\nEdad Promedio por Departamento:\n')
        f.write(edad_prom.to_string())
