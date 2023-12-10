num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

temporal = 0

while num2 != 0:
    temporal = num2
    num2 = num1 % num2
    num1 = temporal

print(f"El mcd es {num1}")
        