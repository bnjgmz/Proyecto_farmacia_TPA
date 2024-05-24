import tkinter as tk
from tkinter import messagebox
import json

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

def cargar_productos_desde_json():
    try:
        with open("productos.json", "r") as archivo:
            datos = json.load(archivo)
            productos = []
            for producto in datos:
                productos.append(Producto(producto["nombre"], producto["precio"], producto["cantidad"]))
            return productos
    except FileNotFoundError:
        return []

def guardar_productos_en_json(productos):
    datos = []
    for producto in productos:
        datos.append({"nombre": producto.nombre, "precio": producto.precio, "cantidad": producto.cantidad})
    with open("productos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def añadir_producto():
    def agregar_producto():
        nombre = nombre_entry.get()
        precio = float(precio_entry.get())
        cantidad = int(cantidad_entry.get())
        productos.append(Producto(nombre, precio, cantidad))
        guardar_productos_en_json(productos)
        messagebox.showinfo("Éxito", "Producto añadido con éxito.")
        ventana_agregar.destroy()

    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Añadir Producto")

    tk.Label(ventana_agregar, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    nombre_entry = tk.Entry(ventana_agregar)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana_agregar, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
    precio_entry = tk.Entry(ventana_agregar)
    precio_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana_agregar, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5)
    cantidad_entry = tk.Entry(ventana_agregar)
    cantidad_entry.grid(row=2, column=1, padx=5, pady=5)

    agregar_button = tk.Button(ventana_agregar, text="Agregar", command=agregar_producto)
    agregar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def buscar_producto():
    pass

def modificar_producto():
    pass

def vender_producto():
    pass

def ver_productos():
    pass

def salir():
    root.destroy()

root = tk.Tk()
root.title("Gestión de Inventario de Farmacia")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Opciones", menu=file_menu)
file_menu.add_command(label="Añadir Producto", command=añadir_producto)
file_menu.add_command(label="Buscar Producto", command=buscar_producto)
file_menu.add_command(label="Modificar Producto", command=modificar_producto)
file_menu.add_command(label="Vender Producto", command=vender_producto)
file_menu.add_command(label="Ver Productos", command=ver_productos)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=salir)

productos = cargar_productos_desde_json()

root.mainloop()
