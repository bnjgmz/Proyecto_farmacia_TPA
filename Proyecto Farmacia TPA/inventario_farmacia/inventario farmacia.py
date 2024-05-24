import json
import tkinter as tk

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        return [producto.mostrar_informacion() for producto in self.productos]

# Función para cargar datos desde un archivo JSON
def cargar_datos_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos_json = json.load(archivo)
    return datos_json

# Crear instancias de productos desde los datos JSON
def crear_productos_desde_json(datos_json):
    productos = []
    for producto_json in datos_json["productos"]:
        producto = Producto(producto_json["nombre"], producto_json["precio"], producto_json["cantidad"])
        productos.append(producto)
    return productos

# Cargar datos desde el archivo JSON "listado.json"
datos_json = cargar_datos_desde_json("listado.json")

# Crear instancias de productos desde los datos JSON
productos = crear_productos_desde_json(datos_json)

# Agregar productos al inventario
inventario = Inventario()
for producto in productos:
    inventario.agregar_producto(producto)

# Funciones de los botones
def mostrar_inventario():
    resultado_label.config(text="\n".join(inventario.mostrar_inventario()))

def buscar_producto():
    nombre = nombre_entry.get()
    for producto in inventario.productos:
        if producto.nombre.lower() == nombre.lower():
            resultado_label.config(text=producto.mostrar_informacion())
            return
    resultado_label.config(text="Producto no encontrado")

def agregar_modificar_producto():
    nombre = nombre_entry.get()
    precio = int(precio_entry.get())
    cantidad = int(cantidad_entry.get())
    for producto in inventario.productos:
        if producto.nombre.lower() == nombre.lower():
            producto.precio = precio
            producto.cantidad = cantidad
            resultado_label.config(text="Producto modificado")
            return
    inventario.agregar_producto(Producto(nombre, precio, cantidad))
    resultado_label.config(text="Producto añadido")

def eliminar_producto():
    nombre = nombre_entry.get()
    for producto in inventario.productos:
        if producto.nombre.lower() == nombre.lower():
            inventario.productos.remove(producto)
            resultado_label.config(text="Producto eliminado")
            return
    resultado_label.config(text="Producto no encontrado")

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de inventario de farmacia")

nombre_label = tk.Label(root, text="Nombre del producto:")
nombre_label.grid(row=0, column=0, sticky="w")

nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

precio_label = tk.Label(root, text="Precio:")
precio_label.grid(row=1, column=0, sticky="w")

precio_entry = tk.Entry(root)
precio_entry.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad:")
cantidad_label.grid(row=2, column=0, sticky="w")

cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

mostrar_button = tk.Button(root, text="Mostrar inventario", command=mostrar_inventario)
mostrar_button.grid(row=3, column=0)

buscar_button = tk.Button(root, text="Buscar producto", command=buscar_producto)
buscar_button.grid(row=3, column=1)

agregar_modificar_button = tk.Button(root, text="Agregar/Modificar producto", command=agregar_modificar_producto)
agregar_modificar_button.grid(row=4, column=0)

eliminar_button = tk.Button(root, text="Eliminar producto", command=eliminar_producto)
eliminar_button.grid(row=4, column=1)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=5, columnspan=2)

root.mainloop()
