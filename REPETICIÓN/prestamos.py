# Solicitar al usuario el monto del prestamo , la tasa de interes anual y el plazo de meses

montPresta = float(input('Ingrese el monto del prestamo: $'))
tasInteresAnual= float(input('Ingrese la tasa de interes anual (en porcentaje): '))
plazoMeses= float(input('Ingrese el plazo de prestamo en meses: '))

# convertir la tasa de interes anual de interes mensual

tasInteresMensual=(tasInteresAnual / 100) / 12

#calcular el pago mensual utilizando la formula

pagoMensual= (montPresta * tasInteresMensual) / (1- (1 + tasInteresMensual) ** -plazoMeses)

#Mostrar el pago mensual

print(f'El pago mensual necesario para pagar el prestamo en {plazoMeses} meses es: ${pagoMensual:.2f}')

