# Importar la librería tkinter para la interfaz gráfica
import tkinter as tk
from tkinter import  messagebox
import json

# Definición de la clase Producto que representa un producto en el inventario
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

# Mensaje de bienvenida al programa
print('Bienvenido al programa de gestión de inventarios'.center(60, '-'))

# Crear una lista de productos inicializados con valores
productos = [
    Producto("bion 3 mini", 10990, 10),
    Producto("Muno probioticos+Vitaminas 30 comprimidos", 13990, 20),
    Producto("tapsin plus noche parecetamol 650mg", 600, 100),
    Producto("Tapsin plus dia Parecetamol 650 mg solucion oral 1 sobre", 600, 50),
    Producto("Genion Caliente dia Parecetamol mg 1 Sobre", 414, 80),
    Producto("Tapsin noche compuesto antigripal Parecetamol 400mg", 414, 60),
    Producto("Abilar Hedera Helix '.7 gra Jarabe 100ml", 4312, 30),
    Producto("Fisiolimp Cloruro De Sodio 0.9 Solucion Nasal", 3990, 40),
    Producto("Bildren Bilastina 20 mg 30 Comprimidos", 17112, 15),
    Producto("Alexia Forte Fexofenadina 180 mg 30 Comprimidos Recubierto", 22952, 10),
    Producto("Bisolvon Jarabe Adutlos 125 ml", 3096, 25),
    Producto("Vaporub Mentol 1.36% Topico 50 gr", 3752, 35),
    Producto("Redoxon Doble Accion Sabor Naranja", 3112, 45),
    Producto("Muxol adulto Ambroxol 30 mg 5ml  Jarabe", 3690, 20),
    Producto("Paltomiel Adulto Eucalipt 4% jarabe 200 ml", 3290, 30)
]

# Función para vender un producto
def vender_producto(nombre):
    global productos
    for producto in productos:
        if producto.nombre == nombre:
            if producto.cantidad > 0:
                producto.cantidad -= 1
                print(f"Venta realizada con éxito. Quedan {producto.cantidad} unidades de {producto.nombre} en inventario.")
            else:
                print("No hay suficientes productos en inventario para realizar la venta.")
            return
    print("Producto no encontrado.")

# Bucle principal para interactuar con el usuario
while True:
    # Mostrar las opciones disponibles
    print("""
    (1) Añadir producto
    (2) Buscar producto
    (3) Modificar producto
    (4) Vender producto
    (5) Ver productos
    (6) Salir
    """)

    # Pedir al usuario que ingrese una opción
    respuesta = input('Ingrese su opción: ')
    if respuesta == '1':  # Opción para añadir un producto
        nombre = input('Ingrese el nombre del producto: ')
        precio = float(input('Ingrese el precio del producto: '))
        cantidad = int(input('Ingrese la cantidad de productos: '))
        productos.append(Producto(nombre, precio, cantidad))
        print("Producto añadido con éxito.")
    elif respuesta == '2':  # Opción para buscar un producto
        nombre = input('Ingrese el nombre del producto que quiere buscar: ')
        for producto in productos:
            if producto.nombre == nombre:
                print('Nombre:', producto.nombre)
                print('Cantidad:', producto.cantidad)
                print('Precio:', producto.precio)
                break
        else:
            print("Producto no encontrado.")
    elif respuesta == '3':  # Opción para modificar un producto
        nombre = input('Ingrese el nombre del producto que quiere modificar: ')
        for producto in productos:
            if producto.nombre == nombre:
                producto.precio = float(input('Ingrese el nuevo precio del producto: '))
                producto.cantidad = int(input('Ingrese la nueva cantidad de productos: '))
                print("Producto modificado con éxito.")
                break
        else:
            print("Producto no encontrado.")
    elif respuesta == '4':  # Opción para vender un producto
        nombre = input('Ingrese el nombre del producto que quiere vender: ')
        vender_producto(nombre)
    elif respuesta == '5':  # Opción para ver todos los productos en inventario
        print('Inventario:')
        for producto in productos:
            print('Nombre:', producto.nombre)
            print('Cantidad:', producto.cantidad)
            print('Precio:', producto.precio)
            print()
    elif respuesta == '6':  # Opción para salir del programa
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
 