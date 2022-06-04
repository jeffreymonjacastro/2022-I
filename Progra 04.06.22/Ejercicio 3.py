n = "Arroceria"
cadena = n.lower()

d = {}

# Crear el diccionario con las llaves
for i in cadena:
    d[i] = []

# Agregar valores a cada llaves
for j in range(len(cadena)):
    d[cadena[j]].append(j)

# Imprimir el diccionario en vertical
for k in d.keys():
    print(f"{k}: {d[k]}")
