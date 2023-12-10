num = -1

lista = []
while num == -1:
    res = int(input("Escribe: "))
    if res == 0:
        num = 1
    else:
        lista.append(res)

numBuscar = int(input("Escribe un numero a buscar: "))

posiciones = []
for pos in range(len(lista)):
    posicion = lista.index(numBuscar, pos)
    posiciones.append(posicion)

conjunto = set(posiciones)

print(conjunto)

# print("Esta en las posiciones", lista.index(numBuscar))
# print("Esta en las posiciones", lista.index(numBuscar, lista.index(numBuscar) +1))