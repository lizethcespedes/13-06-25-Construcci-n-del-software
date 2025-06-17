# Listas
print("=== Lista ===")
colores = ["azul", "morado", "rojo", "naranja"]
for color in colores:
    print("- " + color)

print("\n=== Diccionario ===")
# Diccionarios
persona = {
    "Nombre": "Carlos",
    "Edad": 28,
    "Ciudad": "Bogotá",
    "Profesión": "Desarrollador"
}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print("\n=== Tupla ===")
# Tuplas
coordenadas = (12.5, 45.8)
print(f"Latitud: {coordenadas[0]}")
print(f"Longitud: {coordenadas[1]}")

print("\n=== Conjunto ===")
# Conjuntos
lenguajes = {"Python", "JavaScript", "C++", "Go"}
for lenguaje in sorted(lenguajes):  # Se ordena para que se vea bien
    print(f"- {lenguaje}")