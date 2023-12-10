cantidad_pares = 0
cantidad_impares = 0

n = int(input("Escribe la cantidad de números: "))

for i in range(n):
    numero = int(input(f"Numero-> "))
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

print(f"La cantidad de números pares es: {cantidad_pares}")
print(f"La cantidad de números impares es: {cantidad_impares}")

