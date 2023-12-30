def cargar():
    personas={}
    for x in range(4):
        numero=int(input("DNI:"))
        nombre=input("Nombre:")
        personas[numero]=nombre
    return personas


def consulta_por_numero(personas):

    print("Listado del diccionario completo")
    for numero in personas:
        print(numero, personas[numero])


    nro=int(input("Ingrese el numero de documento a consultar:"))
    if nro in personas:
        print("Nombre de la persona:",personas[nro])
    else:
        print("No existe una persona con dicho numero de documento")

personas=cargar()
consulta_por_numero(personas)