# entrada1 = set(input("Ingrese el número de documento del primer miembro: ")) 
entrada1 = "44356376"
# entrada2 = set(input("Ingrese el número de documento del segundo miembro: ")) 
entrada2 = "4341551"

def detectar_digitos_repetidos(cadena_numeros):
    vistos = set()
    repetidos = set()

    for caracter in cadena_numeros:
        if caracter in vistos:
            repetidos.add(caracter)
        else:
            vistos.add(caracter)
    
    return repetidos
repetidos = detectar_digitos_repetidos(entrada1)
repetidos = detectar_digitos_repetidos(entrada2)


entrada1 = set(entrada1)
entrada2 = set(entrada2)
print(f"Conjunto A = {sorted(entrada1)}")
print(f"Conjunto B = {sorted(entrada2)}")

interseccion = entrada1.intersection(entrada2)
union = entrada1.union(entrada2)
diferencia = entrada1.difference(entrada2)
diferencia2 = entrada2.difference(entrada1)
diferenciaSimetrica = entrada1.symmetric_difference(entrada2)


print(f"A U B = {sorted((union))}")
print(f"A ∩ B = {sorted(interseccion)}")
print(f"A - B = {sorted(diferencia)}")
print(f"B - A = {sorted(diferencia2)}")
print(f"A Δ B = {sorted(diferenciaSimetrica)}")


if repetidos:
    print("Dígitos repetidos encontrados:", sorted(repetidos))
else:
    print("No hay dígitos repetidos.")

