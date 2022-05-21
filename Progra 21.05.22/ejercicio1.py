# Elaborar un código que cree una matriz de 3 filas y 3 columnas donde te solicite
# ingresar los elementos y calcule la suma de elementos

#Jeffrey MOnja
DB = [
    fila1 := [],
    fila2 := [],
    fila3 := []
]

for i in range(9):
    n = int(input("Ingrese los valores: "))
    if i%3 == 0:
        fila1.append(n)
    elif i%3 == 1:
        fila2.append(n)
    elif i%3 == 2:
        fila3.append(n)

suma = 0
for i in range(3):
    for j in range(3):
        print(DB[i][j], end="\t")
        suma += DB[i][j]
    print()

print(suma)

###########################################
#Código de profe

M = 3 # numero de filas
N = 3 # numero de columnas

#CREA UNA MATRIZ Y MOSTRAR LOS CEROS
"""
matriz = []
fila = []

for i in range(N):
    fila.append(0)

for i in range(M):
    matriz.append(fila)

for i in range(M):
    for j in range(N):
        print('{:<7}'.format(matriz[i][j]), end=" ")
    print()
"""

matriz = []
for i in range(M):
    fila = []
    for j in range(N):
        mensaje = f"Ingrese el valor de fila {str(i)} columna {str(j)}:"
        x = int(input(mensaje))
        fila.append(x)
    matriz.append(fila)

for i in range(M):
    for j in range(N):
        print('{:<7}'.format(matriz[i][j]), end=" ")
    print()

suma = 0
for i in range(M):
    for j in range(N):
        suma += matriz[i][j]

print(f"la suma es: {suma}")
