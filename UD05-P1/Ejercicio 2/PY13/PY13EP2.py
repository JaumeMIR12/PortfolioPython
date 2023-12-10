oracion = input("Escribe una oración: ")

oracionMin = oracion.lower()

vocales = 0

for letra in oracionMin:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1

print(f"La cantidad de vocales en la oración es: {vocales}")
