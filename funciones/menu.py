import modelos.productos as pstats
import dao.inventario_dao as producto_dao

def menu_principal():
    print("Escoge una opción.")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar cantidad de producto")
    print("5. Listar productos")
    print("6. Salir")

def ejecutar_opcion(opcion):
    dao = producto_dao.productoDAO()

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        id_producto = input("Ingrese el ID del producto: ")
        minimo = int(input("Ingrese la cantidad mínima permitida: "))
        producto = pstats.Producto(id_producto, nombre, cantidad, minimo)
        dao.agregar_producto(producto)
        print("Producto agregado exitosamente.")

    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        id_producto = input("Ingrese el ID del producto a buscar: ")
        producto = dao.buscar_producto(id_producto, nombre)
        if isinstance(producto, str):
            print("Producto no encontrado.")
        else:
            print(f"Producto encontrado: {producto.nombre}, Cantidad: {producto.cantidad}, ID: {producto.id_producto}")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        resultado = dao.eliminar_producto(id_producto, nombre)
        print(resultado)

    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        id_producto = input("Ingrese el ID del producto a actualizar: ")  # se pide pero no se usa
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        resultado = dao.actualizar_cantidad(nombre, nueva_cantidad)
        print(resultado)

    elif opcion == 5:
        productos = dao.listar_productos()
        if productos:
            print("Lista de productos:")
            for producto in productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")

    elif opcion == 6:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

def main():
    while True:
        menu_principal()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 6:
                break
            ejecutar_opcion(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 6.")
