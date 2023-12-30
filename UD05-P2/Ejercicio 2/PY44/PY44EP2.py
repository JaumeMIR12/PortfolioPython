class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        resultado_suma = self.num1 + self.num2
        return resultado_suma

    def resta(self):
        resultado_resta = self.num1 - self.num2
        return resultado_resta

    def multiplicacion(self):
        resultado_multiplicacion = self.num1 * self.num2
        return resultado_multiplicacion

    def division(self):
        if self.num2 != 0:
            resultado_division = self.num1 / self.num2
            return resultado_division
        else:
            return "No es posible dividir por cero"

num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

operaciones = Operaciones(num1, num2)

print("Suma:", operaciones.suma())
print("Resta:", operaciones.resta())
print("Multiplicacion:", operaciones.multiplicacion())
print("Division:", operaciones.division())
