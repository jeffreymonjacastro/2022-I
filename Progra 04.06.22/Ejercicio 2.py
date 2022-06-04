## Mentor forma
cadena = input("Números: ")
separador = int(input("Separador: "))

numeros = []

for i in cadena:
    numeros.append(int(i))
print(numeros)

def SplitList(lista, sep):
    result = []
    cont = 0
    for i in range(len(lista)):
        if lista[i] == sep and cont == 0:
            result.append(lista[:i])
            cont = i + 1
        elif lista[i] == sep:
            result.append(lista[cont:i])
            cont = i + 1
        elif i == len(lista) - 1:
            result.append(lista[cont:])
    return result

print(SplitList(numeros, separador))

## Forma teacher

# list = [5,2,0,1,3,6,0,4,6]
# separator = 0
#
# def SplitList(lista, sep):
#     result = []
#
#     return result
#
# contador = list.count(separator)
#
# lista_posiciones = []
#
# for i in range(len(list)):
#     if list[i] == separator:
#         lista_posiciones.append(i)
# print(lista_posiciones)
#
#
