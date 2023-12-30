def listade10():
    lista=[]
    for x in range(10):
        v=int(input("Numero: "))
        lista.append(v)
    return lista

def listas(lista):
    listaNegativa=[]
    listaPositiva=[]
    for x in range(len(lista)):
        if lista[x]<0:
            listaNegativa.append(lista[x])
        else:
            if lista[x]>0:
                listaPositiva.append(lista[x])
    return [listaNegativa,listaPositiva]                
           

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])

lista=listade10()
listaNegativa,listaPositiva=listas(lista)
print("Lista con los valores negativos")
imprimir(listaNegativa)
print("Lista con los valores positivos")
imprimir(listaPositiva)