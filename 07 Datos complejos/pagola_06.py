# Los ejercicios del 1 al 3 estan en el siguiente bloque de codigo
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añado frutas
# precios_frutas["Naranja"] = precios_frutas.get("", 1200)
# precios_frutas["Manzana"] = precios_frutas.get("", 1500)
# precios_frutas["Pera"] = precios_frutas.get("", 2300) 
precios_frutas.update({"Naranja": 1200, "Manzana": 1500, "Pera": 2300})

# Actualizo precios
# precios_frutas["Banana"] = precios_frutas.get("", 1330)
# precios_frutas["Manzana"] = precios_frutas.get("", 1700)
# precios_frutas["Melón"] = precios_frutas.get("", 2800)
precios_frutas.update({"Banana": 1330, "Manzana": 1700, "Melón": 2800})

print(precios_frutas.items()) #Fruta y precios
print(precios_frutas.keys()) #Solo frutas


# 4
contactos = {}
contacto = 0
for contacto in range(0, 5):
    contacto = contacto + 1
    contactos.setdefault(input("Ingrese el nombre del contacto: "), int(input("Ingrese el número del contacto: ")))

# print(contactos.items())
# print(f"Ha guardado {contacto} contactos")

busqueda = input("Ingrese el nombre del contacto para acceder a su numero: ")
if busqueda in contactos:
    print(f"El numero del contacto es:", contactos.get(busqueda))


# 5
frase = str(input("Ingrese una frase: "))
palabras = frase.split()
palabrasUnicas = set(palabras)
print(palabrasUnicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)


# 6
alumnos = {}

for _ in range(2):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = [
        int(input("Ingrese la primera nota: ")),
        int(input("Ingrese la segunda nota: ")),
        int(input("Ingrese la tercera nota: "))
    ]
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: Notas = {notas}, Promedio = {promedio}")


# 7
parcial1 = {"Ana", "Luis", "Marta", "Pedro", "Sofía"}
parcial2 = {"Luis", "Pedro", "María", "Carlos", "Sofía"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


# 8

stock = {
    "tornillos": 10,
    "martillos": 15,
    "clavos": 35
}

while True:
    producto = input("Ingrese el nombre del producto (o escriba 'salir' para terminar): ").lower()

    if producto == "salir":
        print(f"El stock final es = ", stock)
        break

    if producto in stock:
        print(f"Stock actual de '{producto}': {stock[producto]}")
        agregar = input("¿Desea agregar unidades al stock? (s/n): ").lower()
        if agregar == "s":
            try:
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                stock[producto] += cantidad
                print(f"Stock actualizado de '{producto}': {stock[producto]}")
            except ValueError:
                print("Cantidad inválida.")
    else:
        print(f"El producto '{producto}' no existe en el stock.")
        agregar_nuevo = input("¿Desea agregarlo al stock? (s/n): ").lower()
        if agregar_nuevo == "s":
            try:
                cantidad = int(input("Ingrese la cantidad inicial: "))
                stock[producto] = cantidad
                print(f"Producto '{producto}' agregado con stock {cantidad}.")
            except ValueError:
                print("Cantidad inválida.")


# 9
agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "14:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Entrenamiento",
    ("viernes", "18:30"): "Cena con amigos"
}


dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")
evento = agenda.get((dia, hora))

if evento:
    print(f"Actividad para el {dia} a las {hora}: {evento}")
else:
    print(f"No hay actividad registrada para el {dia} a las {hora}.")


# 10
original = {"Argentina": "Buenos Aires", "Brasil": "Rio", "Chile": "Santiago"}

invertido = {capital: pais for pais, capital in original.items()}

print(f"Diccionario original", original)
print("Diccionario invertido:", invertido)
