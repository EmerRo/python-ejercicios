# Función para calcular el salario neto
def calcular_salario_neto(salario_por_hora, horas_trabajadas, deducciones, impuestos):
    salario_bruto = salario_por_hora * horas_trabajadas
    salario_neto = salario_bruto - deducciones - (salario_bruto * impuestos)
    return salario_neto

# Solicitar al usuario los detalles del empleado
salario_por_hora = float(input("Ingrese el salario por hora: $"))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
deducciones = float(input("Ingrese las deducciones: $"))
impuestos = float(input("Ingrese la tasa de impuestos (%): ")) / 100

# Calcular el salario neto
salario_neto = calcular_salario_neto(salario_por_hora, horas_trabajadas, deducciones, impuestos)

# Mostrar el salario neto
print(f"\nEl salario neto después de impuestos es: ${salario_neto:.2f}")
