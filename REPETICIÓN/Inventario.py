# Inicializar el inventario como un diccionario vacío
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))

    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad

# Función para actualizar la cantidad disponible de un producto
def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))
        inventario[nombre] = nueva_cantidad
        print(f"La cantidad disponible de {nombre} se ha actualizado a {nueva_cantidad}.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para realizar una venta
def realizar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")
    if nombre in inventario:
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        if cantidad_vendida <= inventario[nombre]:
            inventario[nombre] -= cantidad_vendida
            print(f"Venta realizada. Quedan {inventario[nombre]} unidades de {nombre} en stock.")
        else:
            print("Cantidad insuficiente en stock para realizar la venta.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para mostrar el inventario actualizado
def mostrar_inventario():
    print("Inventario actualizado:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

# Menú principal
while True:
    print("\nMenú de Opciones:")
    print("1. Agregar Producto")
    print("2. Actualizar Cantidad")
    print("3. Realizar Venta")
    print("4. Mostrar Inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_cantidad()
    elif opcion == "3":
        realizar_venta()
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") 