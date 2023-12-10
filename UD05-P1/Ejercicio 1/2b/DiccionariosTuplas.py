diccionario_direcciones = {}

for a in range(4):
    dni = input("Escribe el DNI del usuario: ")
    calle = input("Escribe el nombre de la calle: ")
    numero_puerta = input("Escribe el número de puerta: ")
    numero_piso = input("Escribe el número de piso: ")

    datos_direccion = (calle, numero_puerta, numero_piso)
    diccionario_direcciones[dni] = datos_direccion

dni_buscar = input("Escribe un DNI para buscar su dirección: ")

if dni_buscar in diccionario_direcciones:
    direccion = diccionario_direcciones[dni_buscar]
    print(f"La dirección del usuario con DNI {dni_buscar} es: {direccion[0]}, {direccion[1]}, {direccion[2]}")
    #print(f"La dirección del usuario con DNI {dni_buscar} es: {diccionario_direcciones[dni_buscar][0]}, {diccionario_direcciones[dni_buscar][1]}, {diccionario_direcciones[dni_buscar][2]}")
else:
    print("El DNI no se encuentra almacenado.")
