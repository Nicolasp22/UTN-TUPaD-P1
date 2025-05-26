#### B. Operaciones con años de nacimiento ###
year1 = 1989
year2 = 2000

""""·         Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).

·         Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.

·         Si todos nacieron después del 2000, mostrar "Grupo Z".

·         Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

·         Implementar una función para determinar si un año es bisiesto.

·         Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales."""

def contar_par(years):
    par = 0
    impar = 0
    for i in years:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar

def grupo_z(years):
    for i in years:
        if i < 2000:
            return False
    return True

def bisiesto(years):
    for year in years:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "Tenemos uno especial"
    return "Ninguno es biciesto"

def calcular_edad(year):
    return 2025-year

def producto_carteciano(con1, con2):
    con1 = sorted(con1)
    con2 = sorted(con2)
    return[(x,y) for x in con1 for y in con2]

years = (year1, year2)
# print(years)

contar_pares_impares = contar_par(years)
print(f"La cantidad de años pares e impares en {years}es: ")
print("Pares:", contar_pares_impares[0])
print("Impares:", contar_pares_impares[1])

# Grupo z

if grupo_z(years):
    print("Grupo Z")
    
# Bisiesto

print(bisiesto(years))

# Producto cartesiano

print(producto_carteciano(set(str(year1)), set(str(year2))))