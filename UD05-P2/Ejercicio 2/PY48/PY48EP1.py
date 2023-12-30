class Jugador:
    tiempo_fin_juego = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print(f"Jugador: {self.nombre}, Puntaje: {self.puntaje}")

    def pasar_tiempo(self):
        Jugador.tiempo_fin_juego -= 1

jugador1 = Jugador("Carlos", 100)
jugador2 = Jugador("Ana", 50)

while Jugador.tiempo_fin_juego>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_tiempo()
