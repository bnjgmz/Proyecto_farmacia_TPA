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

    def guardar_inventario(self):
        # Aquí puedes implementar el código para guardar el inventario en un archivo o en una base de datos
        print("Inventario guardado correctamente.")

# Crear instancias de productos
producto1 = Producto("Bion 3 mini", 10990, 10)
producto2 = Producto("Muno Probioticos+Vitaminas 30 Comprimidos", 13990, 20)
# Agrega los otros productos aquí

# Agregar productos al inventario
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
# Agrega los otros productos aquí

# Mostrar inventario
inventario.mostrar_inventario()

# Venta de un producto (ejemplo)
inventario.vender_producto("Bion 3 mini", 5)

# Mostrar inventario después de la venta
inventario.mostrar_inventario()

# Agregar un nuevo producto al inventario (ejemplo)
nuevo_producto = Producto("Nuevo producto", 9999, 50)
inventario.agregar_producto(nuevo_producto)

# Mostrar inventario con el nuevo producto
inventario.mostrar_inventario()