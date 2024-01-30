# Crear un diccionario para almacenar la asistencia de los empleados
registro_asistencia = {}

# Solicitar al usuario la cantidad de días en el mes
dias_del_mes = int(input("Ingrese la cantidad de días en el mes: "))

# Solicitar al usuario la lista de empleados
empleados = input("Ingrese los nombres de los empleados separados por coma (por ejemplo, Juan, Maria, Pedro): ").split(',')

# Inicializar el registro de asistencia para cada empleado
for empleado in empleados:
    registro_asistencia[empleado.strip()] = [0] * dias_del_mes

# Registrar la asistencia diaria
for dia in range(1, dias_del_mes + 1):
    print(f"\nRegistro de asistencia para el día {dia}:")
    for empleado in empleados:
        asistencia = input(f"¿{empleado.strip()} asistió al trabajo? (S/N): ").strip().upper()
        if asistencia == 'S':
            registro_asistencia[empleado.strip()][dia - 1] = 1

# Calcular el resumen de asistencia al final del mes
print("\nResumen de Asistencia:")
for empleado, asistencia_diaria in registro_asistencia.items():
    dias_trabajados = sum(asistencia_diaria)
    dias_ausentes = dias_del_mes - dias_trabajados
    asistencia_promedio = (dias_trabajados / dias_del_mes) * 100

    print(f"{empleado}:")
    print(f"Días trabajados: {dias_trabajados}")
    print(f"Días ausentes: {dias_ausentes}")
    print(f"Asistencia promedio: {asistencia_promedio:.2f}%")
    print()
