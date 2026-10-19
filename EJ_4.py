print("Hola, ingresa un numero y te daré su tabla de multiplicar")
a = int(input("¿Qué numero deseas multiplicar?: "))

for i in range(1, 11, 1):
    print(f"{a} x {i} = {a * i}")
