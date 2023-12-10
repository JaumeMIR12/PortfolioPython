lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(f"{lista}")

for f in range(len(lista[0])):
    if lista[0][f]>50:
        lista[0][f]=0

print(f"{lista}")