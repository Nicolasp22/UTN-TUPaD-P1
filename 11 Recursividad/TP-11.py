# 1
num = int(input("Ingrese un número: "))

def factorial(num):
    if num == 0 or num ==1:
      return 1
    else: 
      return num * factorial(num - 1) 

if num > 1:
   print(f"Factoriales del 1 al {num}: ")
   for i in range(1, num + 1):
      print(f"{i}! = {factorial(i)}")


# 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingresá la posición hasta la cual querés ver la serie de Fibonacci: "))

if pos < 0:
    print("Debe ingresar un número mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(f"F({i}) = {fibonacci(i)}")


# 3 
def potencia(b, e):
    if b == 1 or e == 0:
        return 1
    else:
        return b * potencia(b, e-1)
    
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

if e < 0:
    print("El exponente debe ser un numero entero no negativo: ")
else:
    resultado = potencia(b, e)
    print(f"{b} elevado a la exponente {e} es: {resultado}")


# 4
def conversor(num):
    if num == 0:
        return ""
    elif num < 0:
        return "Invalido"
    else:
        return conversor(num//2) + str(num%2)

num=int(input("Ingrese un numero: "))

if num<0:
    print("Ingrese un positivo")
else:
    binario=conversor(num)
    print(f"El numero {num} en binario es {binario}")


# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower().strip()

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')


# 6
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

n = int(input("Ingrese un entero: "))
print(suma_digitos(n)) 



# 7
bloque = int(input("Ingresa la cantidad de bloques: "))
def contar_bloques(bloque):
    if bloque == 1:
       return 1
    else:
        return bloque + contar_bloques(bloque - 1)

print(contar_bloques(bloque))



# 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingresar numero: "))
digito = int(input("Ingresar digito: "))

print(contar_digito(numero, digito))