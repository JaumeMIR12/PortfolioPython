cantidad = int(input("Escribe cantidad de dinero: "))

billetes = [500, 200, 100, 50, 20, 10, 5]

contador = 0

for billete in billetes:
    cantidadBilletes = cantidad // billete # Devuelve la cantidad de billetes de ese valor
    contador += cantidadBilletes # Iré sumando la cantidad de billetes que se necesitan
    cantidad -= cantidadBilletes * billete # Cambio el valor de cantidad restando los billetes usados

print("Numero de billetes:", contador)
