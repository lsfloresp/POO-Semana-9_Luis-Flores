from modelos.producto import Producto

# Clase que gestiona el inventario

class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir producto validando ID único
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Eliminar por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    # Buscar por nombre (parcial)
    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    # Mostrar todo el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        for p in self.productos:
            print(p)
