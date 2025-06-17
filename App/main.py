import tkinter as tk
from tkinter import messagebox
import drector_de_contacto

def agregar_contacto():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()

    if nombre and telefono:
        drector_de_contacto.guardar_contacto(nombre, telefono)
        messagebox.showinfo("Guardado", "Contacto guardado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        mostrar_contactos()
    else:
        messagebox.showerror("Error", "Por favor, completa ambos campos.")

def mostrar_contactos():
    lista.delete(0, tk.END)
    contactos = drector_de_contacto.obtener_contactos()
    for contacto in contactos:
        lista.insert(tk.END, contacto.strip())

ventana = tk.Tk()
ventana.title("MiniAgenda de Contactos")
ventana.geometry("350x400")

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack()

tk.Label(ventana, text="Teléfono:").pack(pady=5)
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.pack()

tk.Button(ventana, text="Agregar contacto", command=agregar_contacto).pack(pady=10)

tk.Label(ventana, text="Contactos guardados:").pack(pady=5)
lista = tk.Listbox(ventana, width=45, height=10)
lista.pack()

mostrar_contactos()

ventana.mainloop()
