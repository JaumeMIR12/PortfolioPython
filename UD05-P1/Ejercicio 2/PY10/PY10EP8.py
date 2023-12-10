suma1 = 0
suma2 = 0
suma3 = 0

for f in range(5):
    edad = int(input("Escribe edad - turno mañana-> "))
    suma1 = suma1 + edad
pro1 = suma1 / 5
print("Promedio - turno mañana:", pro1)

for f in range(6):
    edad = int(input("Escribe edad - turno tarde-> "))
    suma2 = suma2 + edad
pro2 = suma2 / 6
print("Promedio - turno tarde:", pro2)

for f in range(11):
    edad = int(input("Escribe edad - turno noche-> "))
    suma3 = suma3 + edad
pro3 = suma3 / 11
print("Promedio - turno noche:", pro3)

if pro1 > pro2 and pro1 > pro3:
    print("El turno mañana es el que tiene un promedio de edades mayor")
elif pro2 > pro3:
    print("El turno tarde es el que tiene un promedio de edades mayor")
else:
    print("El turno noche es el que tiene un promedio de edades mayor")