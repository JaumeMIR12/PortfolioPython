def contandoMinas(campo):
    filas = len(campo)
    columnas = len(campo[0])

    resultado = []
    for l in range(filas):
        fila = []
        for l in range(columnas):
            fila.append(0)
        resultado.append(fila)

    for i in range(filas):
        for j in range(columnas):
            if campo[i][j] != -1:
                for x in range(max(0, i - 1), min(filas, i + 2)):
                    for y in range(max(0, j - 1), min(columnas, j + 2)):
                        if campo[x][y] == -1:
                            resultado[i][j] += 1

    return resultado

minas = [
    [0, 0, -1, 0, 0],
    [0, -1, -1, 0, 0]
]

resultado = contandoMinas(minas)
for row in resultado:
    print(row)
