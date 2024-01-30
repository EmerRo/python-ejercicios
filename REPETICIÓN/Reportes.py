# Crear un diccionario para almacenar los gastos por categoría
gastos_mensuales = {}

# Solicitar al usuario ingresar los gastos mensuales por categoría
print("Ingrese los gastos mensuales por categoría (ingrese 'fin' para terminar).")

while True:
    categoria = input("Categoría: ").capitalize()
    
    if categoria == 'Fin':
        break
    
    if categoria not in gastos_mensuales:
        gastos_mensuales[categoria] = 0
    
    try:
        monto = float(input("Monto gastado: $"))
        gastos_mensuales[categoria] += monto
    except ValueError:
        print("Ingrese un monto válido.")

# Generar un informe detallado con los totales por categoría
print("\nInforme de Gastos Mensuales:")
for categoria, total in gastos_mensuales.items():
    print(f"{categoria}: ${total:.2f}")
