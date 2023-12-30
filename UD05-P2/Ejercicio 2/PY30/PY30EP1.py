def mayorEdad(*edades):
    mayor = 0
    for edad in edades:
        if edad >= 18:
            mayor += 1
    return mayor

numPer = int(input("Cuantas personas va a introducir: "))

edades = []
for i in range(numPer):
    edad = int(input(f"Edad: "))
    edades.append(edad)

cantidadMayores = mayorEdad(*edades)
print(f"Personas mayores o igual a 18 años --> {cantidadMayores}")
