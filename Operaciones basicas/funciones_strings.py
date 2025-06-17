print("Funciones para Strings")

texto = "Hola, señor locutor"

mayusculas = texto.upper()
minusculas = texto.lower()
longitud = len(texto)
reemplazo = texto.replace("locutor", "persona")

print(f"\nTexto original:       {texto}")
print(f"En mayúsculas:        {mayusculas}")
print(f"En minúsculas:        {minusculas}")
print(f"Longitud del texto:   {longitud} caracteres")
print(f"Reemplazo de palabra: {reemplazo}")
