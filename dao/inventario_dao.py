import pickle
import os

ARCHIVO_BIN = "productos.bin"

class productoDAO:
    def __init__(self):
        self.productos = self._cargar_desde_archivo()

    def _guardar_en_archivo(self):
        with open(ARCHIVO_BIN, "wb") as f:
            pickle.dump(self.productos, f)

    def _cargar_desde_archivo(self):
        if os.path.exists(ARCHIVO_BIN):
            with open(ARCHIVO_BIN, "rb") as f:
                return pickle.load(f)
        return []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self._guardar_en_archivo()

    def obtenerproductos(self):
        return self.productos

    def buscar_producto(self, id_producto, nombre):
        for producto in self.productos:
            if producto.id_producto == id_producto or producto.nombre == nombre:
                return producto
        return "Producto no encontrado"

    def eliminar_producto(self, id_producto, nombre):
        for producto in self.productos:
            if producto.id_producto == id_producto or producto.nombre == nombre:
                self.productos.remove(producto)
                self._guardar_en_archivo()
                return "Producto eliminado"
        return "Producto no encontrado"

    def actualizar_cantidad(self, nombre, cantidad):
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                self.productos[i].cantidad = cantidad
                self._guardar_en_archivo()
                return "Cantidad actualizada"
        return "Producto no encontrado"

    def listar_productos(self):
        return [str(producto) for producto in self.productos]
