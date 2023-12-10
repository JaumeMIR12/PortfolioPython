total_preguntas = int(input("Escribe la cantidad total de preguntas: "))
correctas = int(input("Escribe la cantidad de preguntas correctas: "))

porcentaje_correctas = (correctas / total_preguntas) * 100
nivel = ""

if porcentaje_correctas >= 90:
    nivel = "Nivel máximo"
elif porcentaje_correctas >= 75:
    nivel = "Nivel medio"
elif porcentaje_correctas >= 50:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print(f"El porcentaje de correctas es de {porcentaje_correctas}%")
print(f"Nivel: {nivel}")
