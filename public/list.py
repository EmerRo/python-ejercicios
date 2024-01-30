demo_list=[1,'hello',1.34,True,[1,2,3]]
colors= ['red','green','blue']
# print(demo_list)
numbers_list= list((1,2,3,4))
# print(type(numbers_list))
r= list(range(1,100))
# print(r)
# print(len(colors)) #longuitud o posicionh
# print(len(demo_list)) 
# print(colors[1]) #devuelve la posicion del valor
# print('violet'in colors) #comprueba si un elemento esta en una lista
# print(colors)
# colors[1]='yellow' #cambiar un elemento por otro
# print(colors)
# print(dir(colors)) # ver information de metodos
# colors.append('violet')#me permite agregar un elemento a la lsita
# colors.extend(['violet', 'yellow']) #nos permite agregar varios elementos en una tupla
# colors.extend(['black', 'white']) #nos permite agregar varios elementos en una tupla
# colors.insert(-1 , 'violet')
colors.insert(len(colors),'violet')
print(colors)  

# colors.pop() #elimina el ultimo elemento
# colors.pop(1) #elimina elemento atraves del indice
# colors.remove('red')#elimina elemento seleccionado
# colors.clear()#elimina todo
colors.sort()#ordena alfabeticamente
colors.sort(reverse=True)# ordena inversamente
print(colors.index('red')) # indica en que posicion esta
print(colors.count('red'))#cuenta cuantos elementos hay
print(colors)