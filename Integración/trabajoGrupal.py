numero_user=input("Ingrese un numero entero positivo en formato decimal para convertirlo: ")
hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #lista de los valores hexa para buscarlos por el indice 


if "," in numero_user or "." in numero_user: 
    print("El valor ingresado no es un numero entero.")
    exit()    
if numero_user == "":
    print("No ha ingresado un numero.")
    exit()

numero_user=int(numero_user) 
if numero_user == 0: #si el valor es 0 devolvemos 0 luego de convertirlo a int
    print("El numero decimal 0 equivale a 0 en todos los sistemas.")
    exit()
elif numero_user < 0: 
    print("El valor ingresado no es un numero entero positivo.")
    exit()
else: 
 opciones = input(
    "Indique a qué sistema quiere convertir el número ingresado:\n"
    "  B - Binario\n"
    "  O - Octal\n"
    "  H - Hexadecimal\n"
    "  Z - Todos los anteriores\n"
    "Opción elegida: ")
 if opciones.isdigit(): #si el valor ingresado es un numero devolvemos error
    print("El valor ingresado no es una letra.")
    exit()
 opciones = str(opciones).upper().strip()

 
 if opciones == "B":
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%2))
        numero=numero//2
    final_decimal=''.join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_decimal} en el sistema binario.") #separe cada resultado final para que cuando se piza "Z" se los pueda diferenciar
 elif opciones == "O":
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%8))
        numero=numero//8
    final_octal=''.join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_octal} en el sistema octal.")
 elif opciones == "H":
    resultado=[]
    numero=numero_user
    while numero>0:
        cifra_h=numero%16
        numero=numero//16
        resultado.append(str(hexa[cifra_h]))
    final_hexa="".join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_hexa} en el sistema hexadecimal.")
 elif opciones == "Z":
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%2))
        numero=numero//2
    final_decimal=''.join(reversed(resultado))
    resultado=[]
    numero=numero_user
    while numero>0:
        resultado.append(str(numero%8))
        numero=numero//8
    final_octal=''.join(reversed(resultado))
    resultado=[]
    numero=numero_user
    while numero>0:
        cifra_h=numero%16
        numero=numero//16
        resultado.append(str(hexa[cifra_h]))
    final_hexa="".join(reversed(resultado))
    print(f"El numero decimal {numero_user} equivale a {final_decimal} en el sistema binario, a {final_hexa} en el sistema hexadecimal y a {final_octal} en el sistema octal.")

    
