cantidad = int(input())

numeros = input().split()

numLista = []

for numero in numeros:
    numLista.append(numero)

numLista.reverse()

for numero in numLista:
    print(numero, end=' ')
