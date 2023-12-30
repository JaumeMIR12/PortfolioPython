# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para doblar valores de la lista
def listaDObladaValores(lista):
    for i in range(len(lista)):
        lista[i] *= 2

# Función para devolver una copia de la lista con valores duplicados
def listaCopiadaValoresDoble(lista):
    nueva_lista = lista[:]
    for i in range(len(nueva_lista)):
        nueva_lista[i] *= 2
    return nueva_lista


resultSuma = suma(3, 10)
print(f"La suma es: {resultSuma}")

lista = [1, 2, 3, 4, 5]
print(f"Lista antes de modificar: {lista}")

listaDObladaValores(lista)
print(f"Lista despues de modificar: {lista}")

copLista = listaCopiadaValoresDoble(lista)
print(f"Copia de la lista con valores duplicados: {copLista}")
