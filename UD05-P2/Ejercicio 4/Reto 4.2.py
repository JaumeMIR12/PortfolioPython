def esBisiesto(anyo):
    if anyo % 4 == 0:
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

year = int(input(""))

resultado = esBisiesto(year)
print(resultado)
