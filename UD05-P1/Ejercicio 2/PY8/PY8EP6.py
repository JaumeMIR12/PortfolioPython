sueldo = float(input("Escribe el sueldo: "))
antiguedad = int(input("Escribe años de antigüedad: "))

if sueldo < 500:
    if antiguedad >= 10:
        sueldoPago = sueldo * 1.20
    else:
        sueldoPago = sueldo * 1.05 
else:
    sueldoPago = sueldo

print(f"El sueldo a pagar es:{sueldoPago}")
