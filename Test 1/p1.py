# Bucles anidados - Matriz de coordenadas

n_filas = int(input("Ingrese el numero de filas:"))
n_columnas = int(input("Ingrese el valor de columnas:"))

print("El arreglo de coordenadas es:")

for i in range(1, n_filas + 1):
    for j in range(1, n_columnas + 1):
        print(f"fil:{i}-col:{j}", end="  ")
    print()

print("Jeffrey va a aprobar calculo con 12")

