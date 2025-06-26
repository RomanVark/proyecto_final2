class Producto:
    def __init__(self, id_producto, nombre, cantidad, minimo=15):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.minimo = minimo

    def __str__(self):
        return f"{self.id_producto} - {self.nombre}, ({self.cantidad})"
