# productos = {}
# productos['111A'] = ('111A', 'Monitor LG 22 pulgadas', 99.95)
# productos['222B'] = ('222B', 'Disco duro 512GB SSD', 109.45)
# productos['333C'] = ('333C', 'Ratón bluetooth', 19.35)

# if '111A' in productos:
#     print(productos['111A'][1])

nombre_calle = input("Escribe su nombre de calle: ")
numero_puerta = int(input("Escribe su número de puerta: "))
numero_piso = int(input("Escribe su número de piso: "))

direccion = (nombre_calle, numero_puerta, numero_piso)

print("Nombre de calle:", direccion[0])
print("Número de puerta:", direccion[1])
print("Número de piso:", direccion[2])