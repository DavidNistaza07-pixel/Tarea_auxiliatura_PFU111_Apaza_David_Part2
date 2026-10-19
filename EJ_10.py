print("Bienvenido al sumador, para salir introduzca un numero negativo.")

d = 0
c = int(input("Ingrese un numero: "))

if c < 0:
  print("No se sumo ningun valor, hasta luego!")
else:
  while c >= 0:
    d = d + c 
    c = int(input("Ingrese otro numero: "))
    
  print(f"La suma final es: {d}. Hasta luego!")