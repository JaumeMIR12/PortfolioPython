def numVocales(texto):
    cant=0
    for x in range(len(texto)):
        if texto[x]=="a" or texto[x]=="e" or texto[x]=="i" or texto[x]=="o" or texto[x]=="u":
            cant=cant+1
    print(f"Se ha encontrado {cant} vocal/es en el texto {texto}")


numVocales("Mariano Perez Dominguez")
numVocales("Camarero, una de bravas")
numVocales("Buenas Noches")