contra = 222
a = int(input("Ingrese la contrasenia: "))
while (a < 0):
    print ("La contrasenia es un valor positivo. ")   
    a = int(input("Vuelve a ingresar la contrasenia: "))
while(a != contra):
    
    if (a > contra):
        print ("La contrasenia es menor. ")
    else:
        print ("La contrasenia es superior. ")

    a = int(input("Vuelve a ingresar la contrasenia: "))

print ("Bienvenido, ingresaste al sistema.")