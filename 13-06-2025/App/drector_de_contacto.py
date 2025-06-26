def guardar_contacto(nombre, telefono):
    with open("contactos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {telefono}\n")

def obtener_contactos():
    try:
        with open("contactos.txt", "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []
