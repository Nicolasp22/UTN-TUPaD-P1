from funciones import *

# 1 
imprimir_hola_mundo()

# 2
saludar()

# 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# 5
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

# 6
numero = int(input("Ingrese un numero entero: "))
tabla_multiplicar(numero)

# 7
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
operaciones_basicas(a, b)

# 8
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en M: "))
calcular_imc(peso, altura)

# 9
celsius = float(input("Ingrese la temperatura en grados celsius: "))
celsius_a_fahrenheit(celsius)

# 10
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese otro numero: "))
calcular_promedio(a, b, c)