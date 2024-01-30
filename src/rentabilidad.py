def calcular_rentabilidad(costo_produccion, precio_venta):
    margen_beneficio = ((precio_venta - costo_produccion) / precio_venta) * 100
    return margen_beneficio


print("Calculadora de Rentabilidad de Producto")
print("--------------------------------------")
costo_produccion = float(input("Ingrese el costo de producción del producto: "))
precio_venta = float(input("Ingrese el precio de venta del producto: "))
margen_beneficio = calcular_rentabilidad(costo_produccion, precio_venta)
print("\nResultado de Rentabilidad")
print("-------------------------")
print(f"Costo de producción: ${costo_produccion:.2f}")
print(f"Precio de venta: ${precio_venta:.2f}")
print(f"Margen de beneficio: {margen_beneficio:.2f}%")
if margen_beneficio > 0:
    print("El producto es rentable.")
elif margen_beneficio < 0:
    print("El producto no es rentable.")
else:
    print("El producto es vendido sin margen de beneficio.")