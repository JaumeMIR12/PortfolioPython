texto = input("Ingrese un texto: ")

contador_palabra = 0
inicio = 0

while inicio != -1:
    inicio = texto.find("Python", inicio + 1)
    if inicio != -1:
        contador_palabra += 1

print("Aaparece", contador_palabra, "veces en el texto.")