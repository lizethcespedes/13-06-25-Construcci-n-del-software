import sqlite3

# Conectar base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
conn.commit()

# Funciones CRUD
def crear_usuario(nombre, email):
    try:
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
        conn.commit()
        print("Usuario creado exitosamente.")
    except sqlite3.IntegrityError:
        print("Ya existe un usuario con ese email.")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print("\nLista de usuarios:")
    for u in usuarios:
        print(f"ID: {u[0]}, Nombre: {u[1]}, Email: {u[2]}")
    print()

def actualizar_usuario(id, nuevo_nombre, nuevo_email):
    cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nuevo_nombre, nuevo_email, id))
    if cursor.rowcount > 0:
        conn.commit()
        print("Usuario actualizado.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

# Menú interactivo
while True:
    print("""
====== MENÚ CRUD ======
1. Crear usuario
2. Listar usuarios
3. Actualizar usuario
4. Eliminar usuario
5. Salir
""")
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("Email: ")
        crear_usuario(nombre, email)

    elif opcion == "2":
        listar_usuarios()

    elif opcion == "3":
        listar_usuarios()
        id = int(input("ID del usuario a actualizar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_email = input("Nuevo email: ")
        actualizar_usuario(id, nuevo_nombre, nuevo_email)

    elif opcion == "4":
        listar_usuarios()
        id = int(input("ID del usuario a eliminar: "))
        eliminar_usuario(id)

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")
