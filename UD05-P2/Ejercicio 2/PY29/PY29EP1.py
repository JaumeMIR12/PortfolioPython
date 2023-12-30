def tablaMu(valor, termino=10):
    print(f"Tabla de multiplicar del {valor} hasta el término {termino}:")
    for i in range(1, termino + 1):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")

num = int(input("¿Qué tabla de multiplicar quieres ver? "))
tablaMu(num)
