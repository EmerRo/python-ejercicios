# Función para calcular el monto a pagar
def calcular_nomina(salario_hora, horas_trabajadas):
    # Verificar si hay horas extras (más de 40 horas a la semana)
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario_base = 40 * salario_hora
        salario_extra = horas_extras * (salario_hora * 1.5)  # Se paga 1.5 veces la tarifa normal por horas extras
        monto_total = salario_base + salario_extra
    else:
        monto_total = horas_trabajadas * salario_hora

    return monto_total

# Solicitar al usuario el salario por hora y las horas trabajadas
salario_hora = float(input("Ingrese el salario por hora: $"))
horas_trabajadas = float(input("Ingrese las horas trabajadas en una semana: "))

# Calcular la nómina
nomina = calcular_nomina(salario_hora, horas_trabajadas)

# Mostrar el monto a pagar
print(f"El monto a pagar es: ${nomina:.2f}")