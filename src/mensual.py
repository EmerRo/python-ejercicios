
print("Calculadora de Ingresos y Gastos Mensuales")
print("-----------------------------------------")
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
numero_gastos = int(input("Ingrese el número de gastos regulares: "))
gastos_totales = 0
#Mediante un bucle for, recopila los nombres y montos de cada gasto regular y calcula el total de gastos.
for i in range(numero_gastos):
    nombre_gasto = input(f"Ingrese el nombre del gasto {i + 1}: ")
    monto_gasto = float(input(f"Ingrese el monto del gasto de {nombre_gasto}: "))
    gastos_totales += monto_gasto

balance = ingresos_mensuales - gastos_totales
print("------------------")
print("Reporte Financiero")
print("------------------")
print(f"Ingresos mensuales: ${ingresos_mensuales:.2f}")
print(f"Gastos totales: ${gastos_totales:.2f}")
print("------------------")
if balance > 0:
     print('El balance final es: ')
     print(f"Balance: Excedente de ${balance:.2f}")
elif balance < 0:
     print('El balance final es ')
     #Cantidad que falta a los ingresos para que se equilibren con los gastos
     print(f"Balance: Déficit de ${abs(balance):.2f}")
else:
    print('El balance final es ')
    print("Balance: Equilibrado")