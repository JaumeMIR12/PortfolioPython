def numeroPatrones(texto):
    texto = texto.upper()
    patrones = ["00", "101", "ABC", "HO"]
    
    contador = 0

    for patron in patrones:
        i = texto.find(patron)
        while i != -1:
            contador += 1
            i = texto.find(patron, i + 1)

    return contador

cadena = input()
resultado = numeroPatrones(cadena)
print(resultado)

