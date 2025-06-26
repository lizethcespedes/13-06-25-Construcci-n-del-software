x = float(input("Ingresa el valor de x: "))
y = float(input("Ingresa el valor de y: "))

igual = x == y
diferente = x != y
mayor = x > y
menor = x < y
mayor_igual = x >= y
menor_igual = x <= y

print("\nResultados de comparación:")
print(f"¿x == y?          ➤ {igual}")
print(f"¿x != y?          ➤ {diferente}")
print(f"¿x > y?           ➤ {mayor}")
print(f"¿x < y?           ➤ {menor}")
print(f"¿x >= y?          ➤ {mayor_igual}")
print(f"¿x <= y?          ➤ {menor_igual}")