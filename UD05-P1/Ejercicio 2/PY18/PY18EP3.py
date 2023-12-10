lista = []

for i in range(5):
    elemento = int(input("Escribe un número: "))
    lista.append(elemento)

lista.sort()
print(f"Lista ordenada de menor a mayor: {lista}")

lista.sort(reverse=True)
print(f"Lista ordenada de mayor a menor: {lista}")