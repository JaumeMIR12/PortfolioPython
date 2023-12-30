from personalhospital import PersonalHospital

class Enfermero(PersonalHospital):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta