# diccionario
inventario = {}

# producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    precio = float(input("Ingrese el precio por unidad: "))
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}

# Función para actualizar la cantidad en stock de un producto
def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        inventario[nombre]["cantidad"] = nueva_cantidad
        print(f"La cantidad en stock de {nombre} se ha actualizado a {nueva_cantidad}.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para realizar una venta
def realizar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")
    if nombre in inventario:
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        if cantidad_vendida <= inventario[nombre]["cantidad"]:
            inventario[nombre]["cantidad"] -= cantidad_vendida
            total_venta = cantidad_vendida * inventario[nombre]["precio"]
            print(f"Venta realizada. Total: ${total_venta:.2f}")
        else:
            print("Cantidad insuficiente en stock para realizar la venta.")
    else:
        print("Producto no encontrado en el inventario.")

# Función para generar un informe de inventario
def generar_informe():
    print("Inventario actualizado:")
    for producto, detalles in inventario.items():
        print(f"Producto: {producto}, Cantidad en Stock: {detalles['cantidad']}, Precio por Unidad: ${detalles['precio']}")

# Menú principal
while True:
    print("\nMenú de Opciones:")
    print("1. Agregar Producto")
    print("2. Actualizar Cantidad")
    print("3. Realizar Venta")
    print("4. Generar Informe de Inventario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_cantidad()
    elif opcion == "3":
        realizar_venta()
    elif opcion == "4":
        generar_informe()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
