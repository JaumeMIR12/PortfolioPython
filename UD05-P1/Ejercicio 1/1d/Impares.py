numero = int(input("Escribe un numero: "))

for i in range(1, numero):
    if i % 2 != 0:
        print(f"{i}," , end="")