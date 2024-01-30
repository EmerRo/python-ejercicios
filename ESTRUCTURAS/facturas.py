

def generar_factura():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    fecha_factura = input("Ingrese la fecha de la factura (DD/MM/AAAA): ")

    detalles_productos = []

    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break

        cantidad = int(input("Ingrese la cantidad vendida: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))

        total_producto = (cantidad* precio_unitario)

        detalles_productos.append((nombre_producto, cantidad, precio_unitario, total_producto))

    total_a_pagar = sum(total for (_, _, _, total) in detalles_productos)

   
    print("\n===== Factura =====")
    print(f"Cliente: {nombre_cliente}")
    print(f"Dirección: {direccion_cliente}")
    print(f"Fecha: {fecha_factura}\n")

    print("Detalles de los productos:")
    for i, (nombre, cantidad, precio, total) in enumerate(detalles_productos, start=1):
        print(f"{i}. {nombre}: Cantidad: {cantidad}, Precio Unitario: ${precio:.2f}, Total: ${total:.2f}")

    print(f"\nTotal a pagar: ${total_a_pagar:.2f}")


generar_factura()