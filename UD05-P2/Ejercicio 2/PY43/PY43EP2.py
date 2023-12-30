class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

    def imprimir(self):
        lado_mayor = max(self.lados)
        print(f"El lado mayor es: {lado_mayor}")

    def equilatero(self):
        if len(set(self.lados)) == 1:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")


lado1 = float(input("Primer lado del triángulo: "))
lado2 = float(input("Segundo lado del triángulo: "))
lado3 = float(input("Tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)
triangulo.imprimir()
triangulo.equilatero()
