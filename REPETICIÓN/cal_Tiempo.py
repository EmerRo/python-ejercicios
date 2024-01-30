from datetime import datetime

# Función para calcular el tiempo de entrega estimado
def calcular_tiempo_entrega(fecha_actual, fecha_envio):
    # Convertir las fechas a objetos datetime
    fecha_actual = datetime.strptime(fecha_actual, "%Y-%m-%d")
    fecha_envio = datetime.strptime(fecha_envio, "%Y-%m-%d")

    # Calcular la diferencia de días entre la fecha de envío y la fecha actual
    dias_entrega = (fecha_envio - fecha_actual).days

    return dias_entrega

# Solicitar al usuario ingresar la fecha actual y la fecha de envío en formato "YYYY-MM-DD"
fecha_actual = input("Ingrese la fecha actual (YYYY-MM-DD): ")
fecha_envio = input("Ingrese la fecha de envío (YYYY-MM-DD): ")

# Calcular el tiempo de entrega estimado
tiempo_entrega = calcular_tiempo_entrega(fecha_actual, fecha_envio)

# Mostrar el tiempo de entrega estimado
if tiempo_entrega > 0:
    print(f"El tiempo de entrega estimado es de {tiempo_entrega} días.")
elif tiempo_entrega == 0:
    print("El pedido se entregará hoy.")
else:
    print("El pedido se entregó antes de la fecha actual.")
