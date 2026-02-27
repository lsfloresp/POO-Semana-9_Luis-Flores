 
# 📦 Sistema Avanzado de Gestión de Inventario – Semana 11

## Descripción
Este proyecto corresponde a la mejora del sistema de gestión de inventario desarrollado en semanas anteriores. 
En esta versión se implementa un sistema avanzado utilizando Programación Orientada a Objetos (POO), colecciones 
en Python y almacenamiento persistente en archivos. 
El sistema permite gestionar productos de una tienda mediante un menú interactivo en consola.

## Programación Orientada a Objetos
El sistema está compuesto por dos clases principales:

**Clase Producto:**  
Contiene los atributos ID (único), nombre, cantidad y precio. 
Se implementan métodos getters y setters para encapsular los datos y permitir su modificación controlada.

**Clase Inventario:**  
Gestiona todos los productos y contiene los métodos para añadir, eliminar, actualizar, 
buscar (por ID y por nombre), mostrar inventario, guardar y cargar datos desde archivo.

## Uso de Colecciones
El sistema utiliza diferentes colecciones para optimizar la gestión del inventario:

- **Diccionario (estructura principal):**  
  Se utiliza un diccionario (`self.productos = {}`) donde la clave es el ID del producto 
  y el valor es un objeto de la clase Producto.  
  Esto permite:
  - Búsqueda rápida por ID (tiempo constante O(1)).
  - Evitar duplicación de identificadores.
  - Acceso directo y eficiente a los productos.

- **Lista:**  
  Se utiliza una lista para almacenar los resultados en la búsqueda por nombre y mostrar 
  coincidencias encontradas.

- **Tupla:**  
  Se utiliza al leer los datos desde el archivo, desempaquetando cada línea en variables 
  (id, nombre, cantidad, precio).

## Almacenamiento en Archivos
El sistema implementa persistencia de datos utilizando el archivo `inventario.txt`.

**Carga de datos:**
- Al iniciar el programa se verifica si el archivo existe.
- Si no existe, se crea automáticamente.
- Se leen las líneas del archivo.
- Cada línea se convierte en un objeto Producto.
- Se almacena en el diccionario usando el ID como clave.

Formato del archivo:
ID;Nombre;Cantidad;Precio

**Guardado de datos:**
Cada vez que se añade, elimina o actualiza un producto, el sistema reescribe el archivo 
con la información actual del diccionario, garantizando que los datos permanezcan actualizados.

## Manejo de Excepciones
Se implementó control de errores para:
- PermissionError (falta de permisos).
- ValueError (líneas corruptas).
- Excepciones generales.

Esto permite que el programa no se detenga inesperadamente y mejore su estabilidad.

## Funcionalidades del Sistema
El menú interactivo permite:
1. Añadir producto  
2. Eliminar producto  
3. Actualizar producto  
4. Buscar producto por ID  
5. Buscar producto por nombre  
6. Mostrar inventario  
7. Salir  

## Conclusión
El sistema avanzado de inventario aplica correctamente los conceptos de Programación Orientada a Objetos, 
utiliza un diccionario como colección principal para optimizar la gestión de datos y emplea almacenamiento 
en archivos para garantizar persistencia. Además, implementa manejo de excepciones para asegurar un 
funcionamiento robusto y estable.