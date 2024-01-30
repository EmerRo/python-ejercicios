import datetime
fa=datetime.datetime.now()

fecha_actual= datetime.datetime.now()
fecha_formateada= f"La fecha actual es {fecha_actual:%Y-%m-%d %H:%M}"
print(fecha_formateada) 
nombre = 'maria'
def saludar ():
    nombre='carlos'
    mensaje=f'hola,{nombre}!'
    print(mensaje)
saludar()
print(f'¡hola de nuevo,{nombre}!')

if True:
    print('esta es la linea de indentacion')
    print('tambien esta dentro del bloque if')
print('Esta linea no esta identica por lo tanto esta fuera del bloque')
i=1
print("el valor de ide es",i)
for i in range (1,5):
    print(f"el valor de ide es {i}")

for j in range (1,15):
    print(f"el valor de ide es {j}")    


for i in range (1,6):
    print(f'el valor de i es {i}')
    if i %2 ==0:
        print('numero part')
        print(i % 2)
    else:
        print('i es impar') 
#         print(i/2)   
i= 5 
print('i es numero par')
print(i %2)

print('i es numero impar')
print('El valor',i/2)