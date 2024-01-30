def calcular_pago_mensual(monto_prestamo, tasa_interes, plazo, frecuencia_pagos):
    # Convierte la tasa de interés anual a mensual
    tasa_mensual = tasa_interes / 12 / 100
    
    # Calcula el número total de pagos
    numero_pagos = plazo * frecuencia_pagos
    
    # Calcula el pago mensual
    pago_mensual = (monto_prestamo * tasa_mensual) / (1 - (1 + tasa_mensual) ** -numero_pagos)
    
    return pago_mensual

def generar_cronograma(monto_prestamo, tasa_interes, plazo, frecuencia_pagos):
    pago_mensual = calcular_pago_mensual(monto_prestamo, tasa_interes, plazo, frecuencia_pagos)
    
    print("Cronograma de Pagos:")
    print("------------------------------------------------")
    print("Mes\tPago Mensual\tPago Principal\tPago Interés\tSaldo Restante")
    print("------------------------------------------------")
    
    saldo_restante = monto_prestamo
    
    for mes in range(1, plazo * frecuencia_pagos + 1):
        interes_mes = saldo_restante * tasa_interes / 12 / 100
        principal_mes = pago_mensual - interes_mes
        saldo_restante -= principal_mes
        
        print(f"{mes}\t{pago_mensual:.2f}\t\t{principal_mes:.2f}\t\t{interes_mes:.2f}\t\t{saldo_restante:.2f}")

# Solicitar al usuario los detalles del préstamo
monto_prestamo = float(input("Ingrese el monto del préstamo: $"))
tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
plazo = int(input("Ingrese el plazo del préstamo en meses: "))
frecuencia_pagos = int(input("Ingrese la frecuencia de los pagos mensuales (por ejemplo, 12 para pagos mensuales): "))

# Calcular y mostrar el pago mensual
pago_mensual = calcular_pago_mensual(monto_prestamo, tasa_interes, plazo, frecuencia_pagos)
print(f"\nEl pago mensual es: ${pago_mensual:.2f}\n")

# Generar el cronograma de pagos
generar_cronograma(monto_prestamo, tasa_interes, plazo, frecuencia_pagos)
