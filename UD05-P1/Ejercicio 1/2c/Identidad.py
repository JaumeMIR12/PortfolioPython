tamano = int(input("Escribe el tamaño de una lista: "))

lista = []

for n in range(tamano):
    print(f"Introduce datos de la fila {n}")

    filas = []

    for datoFila in range(tamano):
        datoFila = int(input("Introduce dato: "))
        filas.append(datoFila)
    
    lista.append(filas)


for num in lista:
    print(num)

n=0
cont=0
for j in lista:
    if lista[n][n] == 1:
        cont+=1
    n+=1

if cont == tamano:
    print("Es una matriz identidad")
else:
    print("No es una matriz identidad")

