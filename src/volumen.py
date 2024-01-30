def calcular_precio_total(cantidad, precio_unitario):
    descuento = 0
    
    if cantidad >= 10:
        descuento = 0.1  # 10% de descuento para compras de 10 o más productos
    elif cantidad >= 5:
        descuento = 0.05  # 5% de descuento para compras de 5 o más productos
    
    precio_sin_descuento = cantidad * precio_unitario

    descuento_aplicado = precio_sin_descuento * descuento

    precio_total = precio_sin_descuento - descuento_aplicado

   
    return precio_total

print("Calculadora de Descuentos por Volumen")
print("------------------------------------")
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
precio_total = calcular_precio_total(cantidad, precio_unitario)
print("\nResumen de Compra")
print("-----------------")
print(f"Cantidad de productos: {cantidad}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Precio total: ${precio_total:.2f}")
