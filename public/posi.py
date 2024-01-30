def es_primo(num):
    if num <=1:
        return False
    for i in range(2, int(num **0.5)+1):
        if num % 1 ==0:
            return False
    return True
limite = int(input('ingresa un numero entero positivo: '))


print('Numeros primos menores que', limite, ":")
for num in range(2, limite):
    if es_primo(num):
        print(num)