class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto


class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
        self.intereses = 0


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasaIntereses):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasaIntereses = tasaIntereses

caja_ahorro = CajaAhorro("Christian", 500)
plazo_fijo = PlazoFijo("Navarro", 1000, 60, 0.21)

print("Cuenta de Caja de Ahorro:")
print(f"Titular: {caja_ahorro.titular}")
print(f"Monto: {caja_ahorro.monto}")
print(f"Intereses generados: {caja_ahorro.intereses}")

print("\nCuenta de Plazo Fijo:")
print(f"Titular: {plazo_fijo.titular}")
print(f"Monto: {plazo_fijo.monto}")
print(f"Plazo de imposición en días: {plazo_fijo.plazo}")
print(f"Tasa de interés: {plazo_fijo.tasaIntereses}")
