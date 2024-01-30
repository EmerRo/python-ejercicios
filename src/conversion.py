def convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas):
    if moneda_origen in tasas and moneda_destino in tasas:
        equivalente = cantidad * tasas[moneda_destino] / tasas[moneda_origen]
        return equivalente
    else:
        return None


print("Calculadora de Conversión de Moneda")
print("----------------------------------")
tasas = {
    "USD": 1.0,  # Tasa de cambio respecto al dólar estadounidense
    "EUR": 0.92 ,  # Ejemplo de tasa de cambio del euro
    "PEN":3.70,  #tasa de moneda peruana
}

cantidad = float(input("Ingrese la cantidad de dinero: "))
moneda_origen = input("Ingrese la moneda de origen (USD, EUR, PEN.): ").upper()
moneda_destino = input("Ingrese la moneda de destino (USD, EUR, PEN.): ").upper()
equivalente = convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas)
if equivalente is not None:
    print(f"{cantidad:.2f} {moneda_origen} equivale a {equivalente:.2f} {moneda_destino}")
else:
    print("Monedas no compatibles o tasas de cambio no definidas.")

