f = input("Ingresa una frase: ")

v = "AEIOUaeiou"
cont = 0

for i in f:
  if i in v:
    cont += 1

print(f"\nLa frase: {f} contiene {cont} vocales en total.")