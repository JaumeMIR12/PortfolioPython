class PersonalHospital:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Medico(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad

class Enfermero(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta

class Prueba:
    def __init__(self, fecha, medico):
        self.fecha = fecha
        self.medico = medico

class Paciente:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial = []

    def agregar_prueba(self, prueba):
        self.historial.append(prueba)

#Hago una lista de medicos y enfermeros
personal = [
Medico("67124512C", "Dr. Puchi", "Calle 1", "123456789", "Cardiología"),
Medico("98236651R", "Dr. Josemi", "Calle 2", "123456789", "Ginecología"),
Medico("31652454P", "Dr. Navarro", "Calle 3", "123456789", "Cardiología"),
Enfermero("87654321B", "Fermin", "Calle 4", "123456789", "Planta 2"),
Enfermero("33115621E", "Paco", "Calle 5", "123456789", "Planta 6")]

#Creo el paciente al que le vamos agregar las pruebas
paciente1 = Paciente("76215625T", "Luis", "Calle 6", "123456789")

prueba1 = Prueba("2023-12-18", personal[0])
prueba2 = Prueba("2023-12-19", personal[1])
prueba3 = Prueba("2023-12-25", personal[2])

paciente1.agregar_prueba(prueba1)
paciente1.agregar_prueba(prueba2)
paciente1.agregar_prueba(prueba3)

print("Datos del paciente:")
print(f"DNI: {paciente1.dni}")
print(f"Nombre: {paciente1.nombre}")
print(f"Dirección: {paciente1.direccion}")
print(f"Teléfono: {paciente1.telefono}")
print("\nHistorial de pruebas:")
for prueba in paciente1.historial:
    print(f"Prueba dia: {prueba.fecha}")
    print(f"Médico: {prueba.medico.nombre} de {prueba.medico.especialidad}")
    print("----------")
