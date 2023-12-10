listaSueldosMorning = []
listaSueldosAfter = []

for f in range(4):
    sueldo = int(input("Escribe sueldo - turno mañana-> "))
    listaSueldosMorning.append(sueldo)

print(f"Sueldos de los turnos de la mañana-> {listaSueldosMorning}")

for s in range(4):
    sueldo = int(input("Escribe sueldo - turno tarde-> "))
    listaSueldosAfter.append(sueldo)


print(f"Sueldos de los turnos de la mañana-> {listaSueldosAfter}")