def rep(lista):
    #Paso la lista a un conjunto (sin elementos duplicados) si no son iguales devuelve es que si hay repetidos
    if len(lista) == len(set(lista)):
        return False
    else:
        return True

def numeroMayores(lista):
    for i in lista:
        #Compara los numeros de la lista
        if int(i) < 1 or int(i) > 49:
            return True
        else:
            return False

numeros = input("Los numeros de la loteria separados por espacios: ")

lista = numeros.split(" ")

lista.sort()

print(lista)

repetido = rep(lista)

num = numeroMayores(lista)

if repetido:
    print(f"LISTA NO VALIDA\nHay números repetidos")
else:
    print(f"No hay números repetidos")

if num:
    print(f"LISTA NO VALIDA\nHay números menores que 1 o mayores que 49")
else:
    print(f"No hay números menores que 1 o mayores que 49")
