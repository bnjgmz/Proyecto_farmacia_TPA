class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        print("Inventario de la farmacia:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def vender_producto(self, nombre_producto, cantidad_vendida):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad_vendida:
                    producto.cantidad -= cantidad_vendida
                    print(f"Venta realizada: {cantidad_vendida} unidades de {nombre_producto}")
                    self.guardar_inventario()
                    return
                else:
                    print(f"No hay suficientes unidades de {nombre_producto} en stock.")
                    return
        print(f"{nombre_producto} no encontrado en el inventario.")

    def consultar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                print(f"El producto {nombre_producto} existe en el inventario.")
                print(f"Precio: {producto.precio}")
                print(f"Cantidad: {producto.cantidad}")
                return producto.precio  # Retorna el precio del producto si existe
        print(f"No se encontró el producto {nombre_producto} en el inventario.")
        return None  # Retorna None si el producto no existe

    def guardar_inventario(self):
        # Aquí puedes implementar el código para guardar el inventario en un archivo o en una base de datos
        print("Inventario guardado correctamente.")

# Crear instancias de productos
Productos = [
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

# Agregar productos al inventario
inventario = Inventario()
for producto in productos:
    inventario.agregar_producto(producto)

# Mostrar inventario
inventario.mostrar_inventario()

# Bucle para consultar productos múltiples
while True:
    # Solicitar al usuario el nombre del producto a consultar
    nombre_producto = input("Ingrese el nombre del producto que desea consultar (o escriba 'salir' para terminar): ")

    if nombre_producto.lower() == "salir":
        break  # Salir del bucle si el usuario escribe "salir"

    # Consultar si un producto existe y su precio
    inventario.consultar_producto(nombre_producto)