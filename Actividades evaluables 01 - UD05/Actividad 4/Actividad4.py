# El operador is se utiliza para verificar 
# si dos variables apuntan al mismo objeto en 
# memoria, es decir, si hacen referencia al mismo lugar en la memoria.

a = [1, 2, 3]
b = a 

c = [1, 2, 3]

print(a is b)
print(a is c)
print()

# El operador not se utiliza para negar una condición. 
# Devuelve True si la condición es falsa y False si la condición es 
# verdadera.

valor = True
print(not valor)

numero = 10
print(not numero > 50)

print()

# El operador in se utiliza para 
# verificar si un elemento está 
# presente en una lista por ejemplo

lista = [1, 2, 3, 4, 5]

print(3 in lista)
print(6 in lista)

cadena = "Hola, soy Jaume"

print("Jaume" in cadena)
print("Adios" in cadena)
