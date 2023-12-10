entrada = input("Escribe numeros, separados por espacios: ")

suma = 0
numero = 0

for caracter in entrada:
    if caracter != ' ':
        numero = numero * 10 + int(caracter)
    else:
        suma += numero
        numero = 0
suma += numero


print("La suma total es:", suma)