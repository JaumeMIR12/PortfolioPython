lectura = open("personas.txt", "r", encoding="utf-8")
lineas = lectura.readlines()

lista = list()

for linea in lineas:
    lista.append(linea.split(";"))


mayor = ["", 0]

for i in range(len(lista)):
    num = lista[i]
    edad = num[1]

    if int(mayor[1] == 0):
        mayor = [num[0], edad]
    elif int(edad) > int(mayor[1]):
        mayor= [num[0], edad]
        menor = [num[0], int(edad)]
    elif int(menor[1]) > int(edad):
        menor = [num[0], edad]


print(f"Mayor->{mayor}")
print(f"Menor->{menor}")

