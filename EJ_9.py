a = int(input("Introduce un numero y determinare su factorial: "))
f = 1
n = a

while n > 0:
  f = f * n
  n -= 1

print(f"El factorial de {a} es {f}")