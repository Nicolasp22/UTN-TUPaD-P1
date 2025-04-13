import random
from statistics import median

# 1)
for num in range(0,101,2):
    print(num)

# 2)
const = int(input("Ingrese un numero entero: "))
cantidad_digitos = len(str(const))
print(f"El número {const} tiene {cantidad_digitos} dígito(s).")


# 3)
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

    
inicio = min(num1, num2) + 1
fin = max(num1, num2)

if inicio >= fin:
    print("No hay números enteros entre los valores ingresados.")
else:
    total = sum(range(inicio, fin))
    print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {total}")

# 4)
num1 = int(input("Ingrese un numero entero: "))
sumatoria = 0
contador = 0

while num1 != 0:
    sumatoria = sumatoria + num1
    contador = contador + 1
    num1 = int(input("Ingrese un numero entero: "))

print(f"Se ha detenido la ejecución tras {contador} numeros, el acumulado es {sumatoria}")


# 5)
numeroRandom = random.randint(0, 9)
print(numeroRandom)
numero1 = int(input("Adivine el numero del 0 al 9: "))
contador = 1

if numero1 >= 0 and numero1 <= 9:
 while numero1 != numeroRandom:
    contador = contador + 1
    print("Siga intentando")
    numero1 = int(input("Adivine el numero del 0 al 9: "))
else:
  print("El numero ingresado esta fuera del rango")

print(f"Lo logro tras {contador} intentos")


# 6)
for i in range(100, -1, -2):
 print(i)


# 7)
num = int(input("Ingrese un numero positivo: "))

if num > 0:
  total = sum(range(0, num))
  print(total)


# 8) 
pares = 0
impares = 0
positivos = 0
negativos = 0

for numero in range(0, 100):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares = pares + 1
    elif numero % 2 != 0:
        impares = impares + 1
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    
print("\n ")
print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")
print(f"Los numeros positivos son {positivos}")
print(f"Los numeros negativos son {negativos}")


# 9)
numeros = []

for num in range(0, 100):
    num = int(input("Ingrese un numero positivo: "))
    if num > 0:
        numeros.append(num)
    else:
        print("Debe ingresar un numero positivo")

media = int(median(numeros))
print(media)


# 10)
numero = input("Ingrese un número: ")

if numero.isdigit():
    invertido = numero[::-1]
    print(f"El número invertido es: {invertido}")
else:
    print("Por favor, ingrese solo números positivos.")
