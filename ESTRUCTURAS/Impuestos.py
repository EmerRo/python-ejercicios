
def calcular_total_con_impuestos(subtotal, tasa_impuestos):
    impuestos = subtotal * (tasa_impuestos / 100)
    total = subtotal + impuestos
    return total
subtotal = float(input("Ingrese el subtotal de la compra: $"))
tasa_impuestos = float(input("Ingrese la tasa de impuestos (porcentaje): "))
monto_total = calcular_total_con_impuestos(subtotal, tasa_impuestos)
print(f"El monto total a pagar con impuestos es: ${monto_total:.2f}")