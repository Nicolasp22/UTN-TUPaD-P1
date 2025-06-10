# # 1) 
print("Hola mundo")


# 2)
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")


# 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
domicilio = input("Ingrese su país de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}")


# 4)
radio = int(input("Ingrese el radio: "))

area = (radio * radio) * 3.14
perimetro = int( 2 * 3.14 * radio)

print(f"El area es {area} y el perimetro {perimetro}")


# 5)
segundos = float(input("Ingrese los segundos: "))

print(f"{segundos} segundos equivalen a {segundos/60/60} horas")


# 6)
numero = int(input("Ingrese un numero: "))

print(f"Tabla: {numero}, {numero*2}, {numero*3}, {numero*4}, {numero*5}, {numero*6}, {numero*7}, {numero*8}, {numero*9}, {numero*10}")


# 7)
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))

print(f"{numero1 + numero2}, {numero1/numero2}, {numero1 - numero2}, {numero1 * numero2}")


# 8)
altura = float(input("Ingresar altura en cm: "))
peso = float(input("Ingresar peso en kg: "))

alturaMetros = altura/100
print(f"El IMC es {peso/(alturaMetros*alturaMetros)}")


# 9)
temperatura = float(input("Ingrese la temperatura en grados celsius: "))

print(f"La temperatura en Farenheit es: ", ((temperatura*9/5) + 32))


# 10) 
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un otro: "))
num3 = int(input("Ingrese un otro: "))

promedio = round((num1 + num2 + num3)/3)
print(promedio)