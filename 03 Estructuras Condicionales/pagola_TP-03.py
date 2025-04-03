from statistics import mode, median, mean
import random

# 1) 
edad = int(input("Ingrese su edad: "))
if edad >= 18:
     print("Es mayor de edad")
else:
     print("Es menor de edad")

# 2)
notaExamen = float(input("Ingrese su nota: "))
if notaExamen >= 6:
     print("Aprobado")
else: 
     print("Desaprobado")

# 3)
numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
     print("Ha ingresado un número par")
else: 
     print("Por favor, ingrese un número par")     

# 4)
edad = int(input("Ingrese su edad: "))

if edad < 12:      print("Niño")
elif edad >= 12 and edad < 18:
     print("Adolescente")
elif edad >= 18 and edad < 30:
     print("Adulto joven")
else:
     print("Adulto")


# 5)
contraseña = str(input("Ingrese una contraseña que contenga de 8-14 caracteres: "))


if len(contraseña) >= 8 and len(contraseña) <= 14:
     print("Ha ingresado una contraseña correcta")
else: 
     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = int(mean(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
moda = int(mode(numeros_aleatorios))

if media > mediana and mediana > moda:
     print("Sesgo positivo")
elif media < mediana and mediana < moda:
     print("Sesgo negativo")
elif media == mediana and media == moda:
     print("Sin sesgo")
else:
     print("No se pudo determinar")


# 7) 
texto = input("Ingrese una frase o palabra: ")

if texto[-1] in "aeiou":
     texto += "!" 
     print(texto)


# 8) 
nombre = input("Ingrese su nombre: ")
opciones = int(input("Seleccione una opción: "))

if opciones == 1:
     print(nombre.upper())
elif opciones == 2:
     print(nombre.lower())
elif opciones == 3:
     print(nombre.title())
else:
     print("Error, debe elegir entre las opciones 1, 2 y 3")


# 9)

magnitudTerremoto = int(input("Ingrese la magnitud del terremoto en escala Richter: "))

if magnitudTerremoto < 3: 
    print("Muy leve")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4:      
    print("Leve")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5:     
    print("Moderado")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6:
    print("Fuerte")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7:
    print("Muy Fuerte")
else:
    print("Extremo")


# 10)

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))


if hemisferio == "N":
    if (3, 21) <= (mes, dia) <= (6, 20):
        estacion = "primavera"
    elif (6, 21) <= (mes, dia) <= (9, 20):  
        estacion = "verano"
    elif (9, 21) <= (mes, dia) <= (12, 20): 
        estacion = "otoño"
    else:
        estacion = "invierno"
elif hemisferio == "S":
    if (3, 21) <= (mes, dia) <= (6, 20):
        estacion = "otoño"
    elif (6, 21) <= (mes, dia) <= (9, 20):  
        estacion = "invierno"
    elif (9, 21) <= (mes, dia) <= (12, 20):  
        estacion = "primavera"
    else:        
        estacion = "verano"


print(f"Actualmente te encuentras en {estacion}")
