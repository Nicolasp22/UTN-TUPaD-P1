from math import pi

def imprimir_hola_mundo():
    print("Hola mundo!")

def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}!")

# Aca empece a hacerlo mejor

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    area = pi*(radio*radio)
    print(f"El area del circulo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2*pi*radio
    print(f"El perimetro del circulo es: {perimetro}")

def  segundos_a_horas(segundos):
    horas = int((segundos/60)/60)
    print(f"{segundos} segundos equivalen a {horas} horas")

def tabla_multiplicar(numero):
    contador = 1
    for i in range(1, 11):
        resultado = numero * contador
        print(f"{numero} * {contador} = {resultado}")
        contador = contador + 1


def operaciones_basicas(a, b):
    tupla = (f"{a} + {b} = {a + b}", f"{a} - {b} = {a - b}", f"{a} * {b} = {a * b}", f"{a} / {b} = {a / b}")
    print(tupla)

def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    print(f"Tu índice de masa corporal es {imc}")

def celsius_a_fahrenheit(celsius):
    farenheit = celsius * (9/5) + 32
    print(f"{celsius}°C grados celsius equivalen a {farenheit}°F grados farenheit.")

def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    print(f"El promedio es {promedio}")