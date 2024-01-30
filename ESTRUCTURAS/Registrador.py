
def registrar_ventas():
    meta_ventas = float(input("Ingrese la meta de ventas diaria: "))
    ventas_acumuladas = 0

    # Ciclo para ingresar las ventas de cada día de la semana
    for dia in range(1, 8):
        ventas_dia = float(input(f"Ingrese las ventas del día {dia}: "))
        ventas_acumuladas += ventas_dia
        print(f"Total de ventas acumuladas hasta el día {dia}: ${ventas_acumuladas:.2f}")

        # Verificar si se alcanzó o superó la meta
        if ventas_acumuladas >= meta_ventas:
            print(f"Felicidades, has alcanzado la meta de ventas diarias (${meta_ventas:.2f}) en el día {dia}!")
            break

    print(f"Total de ventas acumuladas al final de la semana: ${ventas_acumuladas:.2f}")


registrar_ventas()