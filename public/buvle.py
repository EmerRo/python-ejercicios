# for num in range (1,21,2):
#     print(num)

#calcular la factorial de un numero dado usando un bucle while.

# number=int(input('ingrese un numero: '))
# factorial= 1
# i =1

# while i <=number:
#     factorial *= i
#     i += 1
# print('El factorial de', number, 'es:',factorial)    
# programa  de IMC
peso = float(input('ingresa tu peso en kg: '))
alt= float(input('Ingreso tu altura en metros: '))

imc = peso / (alt ** 2)

if imc < 18.5:
    categoria = 'bajo de peso'
elif 18.5 <= imc < 24.9:
    categoria = 'peso normal'
elif 24.9 <= imc < 29.9:
    categoria='sobrepeso'
else:
    categoria='Obesidad'

print('tu IMC es :', imc)
print('categoria:',categoria)                
