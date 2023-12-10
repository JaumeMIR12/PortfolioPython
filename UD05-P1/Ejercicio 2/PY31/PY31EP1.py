lista = []

for d in range(5):
    valor = int(input("Escribe numero: "))
    lista.append(valor)

mayor = max(lista)
menor = min(lista)

resultado = (mayor, menor)

print(f"El número mayor es {resultado[0]}")
print(f"El número menor es {resultado[1]}")
