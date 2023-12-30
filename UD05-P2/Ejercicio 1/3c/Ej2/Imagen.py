import os.path
from PIL import Image

def esImagen(imagen):
    #Compruebo si existe
    if not os.path.isfile(imagen):
        print("Esa imagen no existe.")
        return

    #Abro la imagen
    imOriginal = Image.open(imagen)

    while True:
        #Si escriben 0 acaba
        ancho = int(input("Ancho (0 para salir): "))
        if ancho == 0:
            break
        alto = int(input("Alto (0 para salir): "))
        if alto == 0:
            break

        nuevaImagen = imOriginal.resize((ancho, alto)) #genero una nueva imagen con las nuevas dimensiones
        nombreNimagen = f"{ancho}_{alto}_{imagen}" #Genero el nuevo nombre que va a tener la imagen
        nuevaImagen.save(nombreNimagen)
        print(f"Imagen guardada como {nombreNimagen}")

nombreImagen = input("Nombre de la imagen a escalar: ")
esImagen(nombreImagen)
