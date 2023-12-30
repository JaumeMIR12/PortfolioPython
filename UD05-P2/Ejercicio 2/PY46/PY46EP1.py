class Socio:
    def __init__(self):
        self.nombre = input("Nombre del socio: ")
        self.antiguedad = int(input(f"Antiguedad de {self.nombre} en años: "))


class Club:
    def __init__(self):
        self.socios = []
        for _ in range(3):
            socio = Socio()
            self.socios.append(socio)

    def imprimir(self):
        socio_mas_antiguo = max(self.socios, key=lambda x: x.antiguedad)
        print(f"El socio con mayor antigüedad en el club es: {socio_mas_antiguo.nombre}")


club = Club()
club.imprimir()
