cantidad = int(input())

primero = int(input())
masAlto = primero
masBajo = primero

for f in range(cantidad - 1):
    numero = int(input())
    
    if numero > masAlto:
        masAlto = numero
    if numero < masBajo:
        masBajo = numero

print(masAlto, masBajo)
