class Paciente:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial = []

    def agregar_prueba(self, prueba):
        self.historial.append(prueba)