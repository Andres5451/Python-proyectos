class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre 
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Actualizar productos")
    print("5. Eliminar productos")
    print("6. Salir")

inventario = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    if opcion == "6":
        print("Saliendo del programa.")
        break
    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            precio = float(input("Ingresa el precio: "))
            if cantidad < 0 or precio < 0:
                raise ValueError("La cantidad y precio deben ser positivos")
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado exitosamente")
        except ValueError as e:
            print(f'Error: entrada no válida')
    elif opcion == "2":
        if not inventario:
            print("El inventario está vacío")
        else:
            print("\nLista de productos:")
            for p in inventario:
                print(f'Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}')
    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre.lower() == nombre_buscar.lower():
                print(f'\nProducto encontrado:')
                print(f'Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}')
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")
    elif opcion == "4":
        nombre_actualizar = input("Ingrese el nombre del producto a actualizar: ")
        encontrado = False
        for p in inventario:
            if p.nombre.lower() == nombre_actualizar.lower():
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad < 0:
                        raise ValueError("La cantidad debe ser positiva")
                    p.cantidad = nueva_cantidad
                    print("Cantidad actualizada exitosamente")
                    encontrado = True
                except ValueError as e:
                    print(f'Error: entrada no válida ')
                break
        if not encontrado:
            print("Producto no encontrado")
    elif opcion == "5":
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for producto in inventario:
            if producto.nombre.lower() == nombre_eliminar.lower():
                inventario.remove(producto)
                print("Producto eliminado exitosamente")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")