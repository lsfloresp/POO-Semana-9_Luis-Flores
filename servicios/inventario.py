import os
from modelos.producto import Producto

# Clase que gestiona el inventario

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {} #Cambio a diccionario
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
                            self.productos[id_p]=(producto) # Diccionario donde la clave es el ID y el valor es el objeto Producto
                        except ValueError:
                            print("Línea corrupta ignorada:", linea)

        except PermissionError:
            print("No hay permisos para leer el archivo.")

    # GUARDAR EN ARCHIVO

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos.values(): # Recorre los valores del diccionario (objetos Producto)
                    linea = f"{p.get_id()};{p.get_nombre()};{p.get_cantidad()};{p.get_precio()}\n"
                    f.write(linea)

        except PermissionError:
            print("No hay permisos para escribir en el archivo.")
        except Exception as e:
            print("Error inesperado:", e)

    # Añade un nuevo producto al inventario utilizando el ID como clave del diccionario.
    # Se valida que el ID no exista para evitar duplicados.
    def agregar_producto(self, producto):

        if producto.get_id() in self.productos:
            print("El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto # Inserta el producto usando su ID como clave
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    # Elimina un producto del inventario utilizando su ID como clave del diccionario.
    # Se verifica que el ID exista antes de eliminarlo.
    def eliminar_producto(self, id_producto):

        if id_producto in self.productos:
            del self.productos[id_producto] # Elimina el producto accediendo directamente por su ID
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualiza la cantidad y/o el precio de un producto usando su ID como clave.
    # Se accede directamente al diccionario para modificar el objeto Producto.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        if id_producto in self.productos:

            producto = self.productos[id_producto] # Acceso directo al producto mediante su ID

            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad) # Actualiza la cantidad si se proporciona un nuevo valor

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio) # Actualiza el precio si se proporciona un nuevo valor

            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre (parcial)
    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos.values(): # Recorre los objetos Producto almacenados en el diccionario
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    # Busca un producto usando acceso directo al diccionario
    def buscar_por_id(self, id_producto):

        if id_producto in self.productos:
            return self.productos[id_producto]  # Retorna el producto si existe
        else:
            return None

    # Mostrar todo el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        for p in self.productos.values(): # Recorre los objetos Producto almacenados en el diccionario
            print(p)
