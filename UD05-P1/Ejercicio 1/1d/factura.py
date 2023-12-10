total = 0
while True:
    precio = float(input("Ingrese el precio (o 0 para finalizar): "))
    if precio == 0:
        break
    total += precio

    print(f"El total de la factura es: ${total:.2f}")
print("El total de la factura es %.2f" % total)