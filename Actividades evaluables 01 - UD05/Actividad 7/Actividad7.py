import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def acelerar(self):
        print("El coche está acelerando.")

    def frenar(self):
        print("El coche está frenando.")

numCoches = int(input("Cuantos coches vas a crear: "))

colores = ["red", "white", "black", "pink", "blue"]
listaCoches = []

for i in range(numCoches):
    matricula = i + 1
    color = random.choice(colores)
    coche = Car(matricula, color)
    listaCoches.append(coche)

print("\nDetalles de los coches:")
for i in range(min(numCoches, 10)):
    listaCoches[i].imprimir()
