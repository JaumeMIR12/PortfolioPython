oracion = input("Escribe una oración: ")

palabras = oracion.split()

espacios = len(palabras) - 1

print(f"Hay {espacios} espacios en blanco en esa oración")
