import matplotlib.pyplot as plt

def generar_grafico(resumen):
    resumen['mean'].plot(kind='bar', title='Salario Promedio por Departamento',
                         ylabel='Salario Promedio ($)', colormap='viridis')
    plt.tight_layout()
    plt.savefig('grafico_salario.png')
    plt.close()
