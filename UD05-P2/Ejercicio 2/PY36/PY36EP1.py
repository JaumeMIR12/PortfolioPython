def cargar():
    empleados = {}
    while True:
        legajo = int(input("Ingrese el número de legajo: "))
        nombre = input("Ingrese el nombre del empleado: ")
        profesion = input("Ingrese la profesión: ")
        sueldo = float(input("Ingrese el sueldo: "))
        
        empleados[legajo] = {
            'Nombre': nombre,
            'Profesión': profesion,
            'Sueldo': sueldo
        }

        continua = input("¿Ingresar datos de otro empleado? [s/n]: ")
        if continua.lower() != 's':
            break

    return empleados

def imprimir(empleados):
    print("Listado completo de empleados")
    for legajo, datos in empleados.items():
        print(legajo, datos['Nombre'], datos['Profesión'], datos['Sueldo'])

def modificar_sueldo(empleados):
    legajo = int(input("Ingrese el número de legajo para buscar empleado: "))
    if legajo in empleados:
        sueldo = float(input("Ingrese nuevo sueldo: "))
        empleados[legajo]['Sueldo'] = sueldo
    else:
        print("No existe un empleado con ese número de legajo")

def imprimir_analistas(empleados):
    print("Listado de empleados con profesión \"analista de sistemas\"")
    for legajo, datos in empleados.items():
        if datos['Profesión'] == "analista de sistemas":
            print(legajo, datos['Nombre'], datos['Sueldo'])


empleados=cargar()
imprimir(empleados)
modificar_sueldo(empleados)
imprimir(empleados)
imprimir_analistas(empleados)