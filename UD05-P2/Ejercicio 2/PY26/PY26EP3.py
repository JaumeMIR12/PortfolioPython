def multiLista(lista):
    producto = 1
    for el in lista:
        producto *= el
    return producto

lista = [4, 3, 10, 8, 17]

result = multiLista(lista)
print(f"El producto de todos los numeros de la lista es: {result}")
