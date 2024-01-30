n = int(input('ingresa la cantidad de numeros de la secuencia fibanacci: '))

fibonacci=[0,1]
while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci [-2])
print('Los primeros', n, 'numeros de la secuencia Fibonacci son: ')    
print(fibonacci)