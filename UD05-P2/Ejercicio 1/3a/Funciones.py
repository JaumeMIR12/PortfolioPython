# Funcion Maximo Comun Divisor
def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

# Funcion es Primo
def esPrimo(a):
    for n in range(2, a):
        if a % n == 0:
            return False
    return True



num = mcd(20, 12)
print(f"El maximo comun divisor es {num}")

for i in range(1, 50):
    primo = esPrimo(i)
    if primo:
        print(f"El numero {i} es primo")
