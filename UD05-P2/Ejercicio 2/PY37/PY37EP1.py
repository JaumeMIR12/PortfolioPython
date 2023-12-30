def cargar_lista():
    lista_enteros = []
    for i in range(10):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        lista_enteros.append(numero)
    return lista_enteros

def obtener_primer_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    print("La lista a la piremra mitad es:", lista)

lista_enteros = cargar_lista()

primer_mitad = obtener_primer_mitad(lista_enteros)
imprimir_lista(primer_mitad)
