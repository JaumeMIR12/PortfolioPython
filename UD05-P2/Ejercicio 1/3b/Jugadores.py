class Jugador:
 
    def __init__(self, nombre, dorsal):
        self.__nombre = nombre
        self.__dorsal = dorsal

    def mostrar(self):
        print(f"{self.__dorsal}. {self.__nombre}")

j1 = Jugador("Pau Gasol", 14)
j1.mostrar()
j2 = Jugador("Michael Jordan", 23)
j2.mostrar()