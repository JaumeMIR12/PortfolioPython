horas = float(input("número de horas trabajadas: "))
precioHora = float(input("precio por hora: "))

if horas <= 35:
    salario1 = horas * precioHora
else:
    horasExtra = horas - 35
    salario1 = 35 * precioHora + horasExtra * precioHora * 1.5

impuestos = 0
if salario1 > 900:
    impuestos += 0.45 * (salario1 - 900)
    salario1 = 900

if salario1 > 500:
    impuestos += 0.25 * (salario1 - 500)
    salario1 = 500

salario2 = salario1 - impuestos

print("El salario neto semanal es:", salario2)
