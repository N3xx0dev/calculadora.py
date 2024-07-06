 
primer_numero = int(input("Dime un numero: "))
segundo_numero = int(input("Dime otro numero: "))


def operacion():
    print("Que operacion vas a querer realizar: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

operacion()

operacion = input("Introduce el numero de la operacion a realizar: ")

if operacion == 1 :
    suma = primer_numero + segundo_numero
    print(f"La suma de {primer_numero} + {segundo_numero} es igual a: {suma}")
else :
    print("No es una opcion a elegir.")

if operacion == 2 :
    resta = primer_numero - segundo_numero
    print(f"La suma de {primer_numero} - {segundo_numero} es igual a: {resta}")
else :
    print("No es una opcion a elegir.")

if operacion == 3 :
    multiplicacion = primer_numero * segundo_numero
    print(f"La suma de {primer_numero} * {segundo_numero} es igual a: {multiplicacion}")
else :
    print("No es una opcion a elegir.")

if operacion == 4 :
    division = primer_numero / segundo_numero
    print(f"La suma de {primer_numero} / {segundo_numero} es igual a: {division}")
else :
    print("No es una opcion a elegir.")

