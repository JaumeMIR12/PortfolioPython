datos = input("Escribe: ")

listaReverse = datos.split(',')

lista = []

for nombre in listaReverse:
    lista.append(nombre)

lista.reverse()

print(lista)