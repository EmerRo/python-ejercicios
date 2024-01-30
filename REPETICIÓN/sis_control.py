import datetime

# Diccionario para almacenar los registros de asistencia de los empleados
registros_asistencia = {}

# Función para registrar la entrada de un empleado
def registrar_entrada(empleado):
    ahora = datetime.datetime.now()
    fecha_actual = ahora.date()
    hora_entrada = ahora.strftime("%H:%M:%S")

    if empleado not in registros_asistencia:
        registros_asistencia[empleado] = []
    
    registros_asistencia[empleado].append({"fecha": fecha_actual, "entrada": hora_entrada})

# Función para registrar la salida de un empleado
def registrar_salida(empleado):
    ahora = datetime.datetime.now()
    hora_salida = ahora.strftime("%H:%M:%S")

    if empleado in registros_asistencia and registros_asistencia[empleado][-1].get("salida") is None:
        registros_asistencia[empleado][-1]["salida"] = hora_salida

# Función para calcular las horas trabajadas de un empleado en una semana
def calcular_horas_trabajadas(empleado, semana):
    horas_trabajadas = 0

    for registro in registros_asistencia.get(empleado, []):
        fecha_registro = registro["fecha"]
        if fecha_registro.strftime("%U") == semana:
            entrada = datetime.datetime.strptime(registro["entrada"], "%H:%M:%S")
            salida = datetime.datetime.strptime(registro["salida"], "%H:%M:%S")
            diferencia = salida - entrada
            horas_trabajadas += diferencia.total_seconds() / 3600  # Convertir a horas

    return horas_trabajadas

# Función para mostrar el informe de horas trabajadas por empleado en una semana
def mostrar_informe(semana):
    print(f"Informe de Horas Trabajadas para la Semana {semana}:")
    for empleado in registros_asistencia:
        horas_trabajadas = calcular_horas_trabajadas(empleado, semana)
        print(f"{empleado}: {horas_trabajadas:.2f} horas")

# Menú principal
while True:
    print("\nMenú de Opciones:")
    print("1. Registrar Entrada")
    print("2. Registrar Salida")
    print("3. Generar Informe Semanal")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        empleado = input("Ingrese el nombre del empleado: ")
        registrar_entrada(empleado)
        print("Entrada registrada con éxito.")
    elif opcion == "2":
        empleado = input("Ingrese el nombre del empleado: ")
        registrar_salida(empleado)
        print("Salida registrada con éxito.")
    elif opcion == "3":
        semana = input("Ingrese el número de semana para el informe: ")
        mostrar_informe(semana)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
