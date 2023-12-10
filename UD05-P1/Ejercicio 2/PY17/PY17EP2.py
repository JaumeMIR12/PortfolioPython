nombres = []
notas = []

for i in range(4):
    nombre = input("Escribe nombre: ")
    nota = int(input("Escribe nota: "))
    nombres.append(nombre)
    notas.append(nota)


buenos = 0

for i in range(4):
    if notas[i] >= 8:
        cond = "Muy Bueno"
        buenos+=1
    elif notas[i] >= 4:
        cond = "Bueno"
    else:
        cond = "Insuficiente"


print(f"Cantidad de alumnos Muy Buenos: {buenos}")