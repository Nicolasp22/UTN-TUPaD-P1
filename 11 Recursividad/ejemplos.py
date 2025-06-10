# def cuenta_regresiva(n):
#     if n ==0:
#         print("Despegue")
#     else:
#         print(n)
#         cuenta_regresiva(n-1)

# cuenta_regresiva(5)


# g = 5
# while g > 0:
#     print(g)
#     g = g - 1

# print("Despegue")

# def sum_list(lista):
#     if len(lista)==0:
#         return 0
#     else:
#         return lista[0] + sum_list(lista[1:])

# lista=[2, 3, 6, 12, 1]

# print(f"el valor total de la lista es {sum_list(lista)}")

# num = int(input())
# frase = "Repeticion"
# def repetir_frase(num,frase):
#     if num >= 1:
#         print(frase)
#         repetir_frase(num-1, frase)

# repetir_frase(num, frase)

# num = int(input())
# def suma_recursiva(num):
#     if num == 0:
#         return 0
#     else:
#         return num + suma_recursiva(num-1)
    
# print(suma_recursiva(num))


# def decimal_a_binario(n):
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return decimal_a_binario(n // 2) + str(n % 2)

# # Solicitar al usuario un número entero positivo
# numero = int(input("Ingresá un número entero positivo: "))

# # Validar que sea positivo
# if numero < 0:
#     print("Debe ingresar un número entero positivo.")
# else:
#     binario = decimal_a_binario(numero)
#     print(f"El número {numero} en binario es: {binario}")


