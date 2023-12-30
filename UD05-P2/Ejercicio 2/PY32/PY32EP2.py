def cargarCandidatos():
    candidatos = []

    for i in range(3):
        nombre = input(f"Candidato {i + 1}: ")
        
        votProvincias = []
        while True:
            provincia = input(f"Ingrese el nombre de la provincia para {nombre} (o 'fin' para terminar): ")
            if provincia == 'fin':
                break

            cantidadvotos = int(input(f"Ingrese la cantidad de votos en {provincia} para {nombre}: "))
            votProvincias.append((provincia, cantidadvotos))

        candidatos.append((nombre, votProvincias))

    return candidatos

def sacarTexto(candidatos):
    for candidato in candidatos:
        nombre = candidato[0]
        total_votos = sum(votos for _, votos in candidato[1])
        print(f"El candidato {nombre} obtuvo un total de {total_votos} votos.")

candidatos = cargarCandidatos()

sacarTexto(candidatos)

