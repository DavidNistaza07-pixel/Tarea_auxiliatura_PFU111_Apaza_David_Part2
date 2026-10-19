print ("Bienvenido al menu interactivo.")
print ("1. Mostrar un Hola Mundo!")
print ("2. Sumar dos numeros.")
print ("3. Determinar si un numero es par o impar.")
print ("4. Mostrar tu edad en 2050.")
print ("0. Salir del menu.")
a = int(input("Elige una opcion: "))
while(a != 0):
    match a:
        case 1:
            print ("Hola Mundo!")

        case 2:
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            print (f"La suma de ambos numeros es {a + b}")

        case 3:
            a = int(input("Ingresa el numero: "))
            if (a % 2 == 0):
                print (f"El numero {a} es par")
            else:
                print (f"El numero {a} es impar")

        case 4:
            a = int(input("Ingresa tu anio de nacimiento: "))
            print (f"En 2050 tendras {2050 - a} anios")

        case _:
            print("Opcion no valida.")

    a = int(input("Elige otra opcion: "))

print("¡Gracias por usar el menú interactivo. Hasta luego!")