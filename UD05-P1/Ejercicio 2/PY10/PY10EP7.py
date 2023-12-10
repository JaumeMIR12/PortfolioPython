neg = 0
posit = 0
multiplos = 0
sumaPares = 0

for i in range(10):
    valor = int(input(f"Escribe un numero-> : "))

    if valor < 0:
        neg += 1
    elif valor > 0:
        posit += 1

    if valor % 15 == 0:
        multiplos += 1

    if valor % 2 == 0:
        sumaPares += valor

print(f"Cantidad de valores negativos: {neg}")
print(f"Cantidad de valores positivos: {posit}")
print(f"Cantidad de múltiplos de 15: {multiplos}")
print(f"Suma de numeros pares: {sumaPares}")
