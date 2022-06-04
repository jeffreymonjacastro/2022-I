def funcion1(lista):
    result = [x**2 for x in lista if x%2 == 0 and x%6 != 0]
    return result

print(funcion1([1,2,3,4,5,6,7,8]))


def funcion2(filas, columnas, valor):
    fila = columnas*[valor]
    matriz = [fila for x in range(filas)]
    return matriz

print(funcion2(3, 5, 9))


def funcion3(lista):
    lista1 = [x for x in lista if x%2 == 0]
    lista2 = [x for x in lista if x%2 != 0]
    return lista1, lista2

print(funcion3([1,2,3,4,5,6,7,8]))


def funcion4(matriz):
    fila = [x for fila in matriz for x in fila]
    return fila

print(funcion4([[1,2],[3,4]]))