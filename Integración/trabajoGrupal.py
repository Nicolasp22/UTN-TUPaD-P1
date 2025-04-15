numero=int(input("Ingrese un numero decimal positivo para convertirlo: "))
resultado=[]
opciones = str(input("Indique a que sistema quiere convertir el numero ingresado (B, O, H): "))
opciones = opciones.upper().strip()

if opciones == "B":
    while numero>0:
        resultado.append(str(numero%2))
        numero=numero//2
        final=''.join(reversed(resultado))
    print(f"El numero decimal {numero} equivale a {final} en el sistema binario.")
elif opciones == "O":
    while numero>0:
        resultado.append(str(numero%8))
        numero=numero//8
        final=''.join(reversed(resultado))
    print(f"El numero decimal {numero} equivale a {final} en el sistema octal.")
elif opciones == "H":
    final = hex(numero)[2:]
    print(f"El numero decimal {numero} equivale a {final} en el sistema hexadecimal.")
else:
    print("Opcion no válida")

