import os
from modelos.producto import Producto

# Clase que gestiona el inventario

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # CARGAR DESDE ARCHIVO

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                return

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(";")
                    if len(datos) == 4:
                        id_p, nombre, cantidad, precio = datos
                        try:
                            producto = Producto(
                                id_p,
                                nombre,
                                int(cantidad),
                                float(precio)
                            )
                            self.productos.append(producto)
                        except ValueError:
                            print("Línea corrupta ignorada:", linea)

        except PermissionError:
            print("No hay permisos para leer el archivo.")

    # GUARDAR EN ARCHIVO

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()};{p.get_nombre()};{p.get_cantidad()};{p.get_precio()}\n"
                    f.write(linea)

        except PermissionError:
            print("No hay permisos para escribir en el archivo.")
        except Exception as e:
            print("Error inesperado:", e)


    # Añadir producto validando ID único
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    # Eliminar por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
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
                self.guardar_en_archivo()
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
