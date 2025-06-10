# Ejercicio 1
lista = list(range(4, 101, 4))

print(lista)


# Ejercicio 2
listado = ["Hola mundo!", 4, "Chau", 5, 8.3, 9]

print(listado[4]) 
print(listado[-2])


# Ejercicio 3
listaVacia =[]
listaVacia.append(["Hola", "mundo!", "chau"])

print(listaVacia)


# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro" 
animales[-1] = "oso" 

print(animales) 


# Ejercicio 5
numeros = [8, 15, 3, 22, 7] 
numeros.remove(max(numeros)) 
print(numeros) 

# 1 se crea la lista de numeros
# 2 se elimina el maximo de la lista
# 3 muestra la lista resultante


# Ejercicio 6
lista = list(range(10, 31, 5))
print(lista[0:2])


# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "civic"
autos[2] = "accord"
print(autos)


# Ejercicio dobles = [dobles.append([5*2, 10*2, 15*2]print(dobles)


# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2][0] = "jugo"
compras[1][1] = "tallarines"
compras[0].remove("pan") 

print(compras) 


# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada[3])