class Equipo:
    def __init__(self, nombreEquipo):
        self.nombreEquipo = nombreEquipo

class Jugador:
    def __init__(self, nombre, dorsal):
        self.__nombre = nombre
        self.__dorsal = dorsal
        self.__equipo = None

    def asignar_equipo(self, equipo):
        self.__equipo = equipo

    def mostrar(self):
        if self.__equipo:
            print(f"{self.__dorsal}. {self.__nombre} Juega en: {self.__equipo.nombreEquipo}")
        else:
            print(f"{self.__dorsal}. {self.__nombre} - Sin equipo asignado")

eq1 = Equipo("Los Angeles Lakers")
eq2 = Equipo("Chicago Bulls")
j1 = Jugador("Pau Gasol", 14)
j2 = Jugador("Michael Jordan", 23)

j1.asignar_equipo(eq1)
j2.asignar_equipo(eq2)

j1.mostrar()
j2.mostrar()
