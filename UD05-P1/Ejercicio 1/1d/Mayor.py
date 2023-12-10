cantidadDeNum = int(input("Dime cuántos números vas a introducir: "))

mayor = 0
for i in range(cantidadDeNum):
    numero = int(input("Numero-> "))
    if mayor == 0:
        mayor = numero
        menor = numero
    elif mayor < numero:
        mayor = numero
    elif menor > numero:
        menor = numero    

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")