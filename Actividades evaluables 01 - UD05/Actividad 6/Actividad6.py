datos = [
    [180, 70],
    [160, 60],
    [170, 65],
    [180, 75],
    [170, 60]
]

# La función de clave, o "key function", 
# toma un elemento de la lista y devuelve un valor 
# basado en el cual se realizará la clasificación.

datosOrdenados = sorted(datos, key=lambda x: (-x[0], x[1]))

print(f"Lista: {datos}")
print(f"Lista ordenada por altura y peso: {datosOrdenados}")


# La "key function" es esencialmente una función que 
# proporciona el criterio sobre el cual se realizará 
# la ordenación, permitiendo personalizar cómo se lleva 
# a cabo la clasificación de los elementos de la lista.

# La key function es como una regla especial 
# que te dice cómo poner los datos en fila. 
# Primero, miras la altura. Los más altos van al principio de la fila 
# y los más bajitos van al final.
# Pero, si hay personas que tienen la misma altura, 
# necesitas otra manera de decidir quién va primero 
# entre esos. Aqui lo que hace key function es comparar si tienen la misma altura, 
# miramos sus pesos.
