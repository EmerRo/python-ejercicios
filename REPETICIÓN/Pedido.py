# Crear un diccionario de productos con precios
productos = {
    "Producto 1": 10.0,
    "Producto 2": 15.0,
    "Producto 3": 20.0,
    "Producto 4": 25.0,
    "Producto 5": 30.0,
}

# Definir la tasa de impuestos y los gastos de envío
tasa_impuestos = 0.08  # 8% de impuestos
gastos_envio = 5.0

# Inicializar el carrito de compras
carrito = {}

# Función para calcular el total del pedido
def calcular_total(carrito, productos, tasa_impuestos, gastos_envio):
    subtotal = sum(productos.get(producto, 0) * cantidad for producto, cantidad in carrito.items())
    impuestos = subtotal * tasa_impuestos
    total = subtotal + impuestos + gastos_envio
    return total

# Mostrar los productos disponibles
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")

# Solicitar al usuario seleccionar productos y cantidades
while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para finalizar el pedido): ")
    
    if producto.lower() == 'fin':
        break
    
    if producto in productos:
        cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
        carrito[producto] = carrito.get(producto, 0) + cantidad
    else:
        print("Producto no válido. Por favor, seleccione un producto de la lista.")

# Calcular el total del pedido
total_pedido = calcular_total(carrito, productos, tasa_impuestos, gastos_envio)

# Mostrar el resumen del pedido
print("\nResumen del Pedido:")
for producto, cantidad in carrito.items():
    precio_unitario = productos[producto]
    subtotal_producto = precio_unitario * cantidad
    print(f"{producto}: {cantidad} unidades - Subtotal: ${subtotal_producto:.2f}")

print(f"\nSubtotal: ${total_pedido - (tasa_impuestos * total_pedido + gastos_envio):.2f}")
print(f"Impuestos ({tasa_impuestos * 100}%): ${tasa_impuestos * total_pedido:.2f}")
print(f"Gastos de Envío: ${gastos_envio:.2f}")
print(f"Total del Pedido: ${total_pedido:.2f}")
