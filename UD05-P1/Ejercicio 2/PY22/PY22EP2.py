lista = []

for i in range(5):
    valor = int(input(f"Numero: "))
    lista.append(valor)

lista2 = []

for num in lista:
     if num >= 10:
          lista2.append(num)


lista3 = []

for ele in lista:
     if ele < 10:
          lista3.append(ele)

print(f"Primera lista -> {lista}")
print(f"Lista con numeros mayores o iguales a 10 -> {lista2}")
print(f"Lista con borrados -> {lista3}")

