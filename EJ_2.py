a = int(input("Bienvenido, ¿cuantos numeros deseas sumar? "))

n = []

for i in range(a):

    x = int(input(f"Ingresa el numero {i + 1}: "))
    
    while (x < 0):
        print("No se admiten numeros negativos.")
        x = int(input(f"Vuelve a ingresar el numero {i + 1}: "))
    
    n.append(x)

s = 0

for z in n:
    s = s + z

print (f"La suma de los numeros{n} es {s}")