# Solicitar al usuario la cantidad inicial de ahorro y la cantidad adicional a ahorrar mensualmente
cantidad_inicial= float(input('Ingrese la cantidad inicial de ahorro: $'))
cantidad_adicional= float(input('Ingrese la cantidad adicional de desea ahorrar cada mes: $ '))

# Inicializar el ahorro total
ahorro_total = cantidad_inicial

# Calcular el ahorro total al final de un año (12 meses)
for mes in range(1, 13):
    ahorro_total += cantidad_adicional

# Mostrar el ahorro total al final de un año
print(f"El ahorro total al final de un año es: ${ahorro_total:.2f}")