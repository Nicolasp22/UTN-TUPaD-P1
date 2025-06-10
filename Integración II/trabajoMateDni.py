entrada1 = input("Ingrese el número de documento del primer miembro: ")
# entrada1 = "44356376"
entrada2 = input("Ingrese el número de documento del segundo miembro: ")
# entrada2 = "34341551"



def digito_compartido(dni1:set, dni2:set):
    return True if dni1.intersection(dni2) else False

def suma_digitos(dni):
    if dni < 10:
        return dni
    else:
        return dni%10 + suma_digitos(dni//10)

def frecuencia_digito(cadena_numero):
    cadena_numero = sorted(cadena_numero)
    frecuencia = {}
    for digito in cadena_numero:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

#DNI ordenados
entrada1_set = set(entrada1)
entrada2_set = set(entrada2)

print(f"Conjunto A = {sorted(entrada1_set)}")
print(f"Conjunto B = {sorted(entrada2_set)}")

#Frecuencia de digitos en DNI
frec_dni1 = frecuencia_digito(entrada1)
frec_dni2 = frecuencia_digito(entrada2)

print(f"La frecuencia de los digitos en el {entrada1} es:")
for i,j in frec_dni1.items():
    print(f"Digito {i}: {j} veces.")
    
print(f"La frecuencia de los digitos en el {entrada2} es:")
for i,j in frec_dni2.items():
    print(f"Digito {i}: {j} veces.")

#Suma de digitos de DNI recursivamente

print(f"La suma de los numeros del DNI {entrada1} es: {suma_digitos(int(entrada1))}")
print(f"La suma de los numeros del DNI {entrada2} es: {suma_digitos(int(entrada2))}")

#Operaciones de conjuntos 
interseccion = entrada1_set.intersection(entrada2_set)
union = entrada1_set.union(entrada2_set)
diferencia = entrada1_set.difference(entrada2_set)
diferencia2 = entrada2_set.difference(entrada1_set)
diferenciaSimetrica = entrada1_set.symmetric_difference(entrada2_set)

print(f"A U B = {sorted(union)}")
print(f"A ∩ B = {sorted(interseccion)}")
print(f"A - B = {sorted(diferencia)}")
print(f"B - A = {sorted(diferencia2)}")
print(f"A Δ B = {sorted(diferenciaSimetrica)}")

#Evaluacion de condiciones logicas
condicion1= entrada2_set.difference(interseccion) #Si A contiene a todos los elementos de B excepto 1
if len(condicion1)==1:
    print(f"El conjunto {sorted(entrada1_set)} es una extencion del conjunto {sorted(entrada2_set)}")

condicion2= entrada1_set.intersection(entrada2_set) #Si la interseccion AyB tiene al menos 3 elementos
if len(condicion2)>= 3:
    print("Los conjuntos son coincidencias significativas")

condicion3 = digito_compartido(entrada1_set, entrada2_set)
if condicion3:
    print("Tiene digitos compartidos")


