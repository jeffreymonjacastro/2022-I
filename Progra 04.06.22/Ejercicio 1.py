# Jeffrey Monja
cadena = "Al que madruga Dios lo ayuda"

cadena_palabras = cadena.split()

cadena_reves = []

## Formas de voltear el orden
# cadena_reves = cadena_palabras[::-1]
#
# for i in range(1, len(cadena_palabras)+1):
#     cadena_reves.append(cadena_palabras[len(cadena_palabras)-i])

for i in range(len(cadena_palabras)-1, -1, -1):
    print(i)
    if i % 2 == 0:
        cadena_reves.append(cadena_palabras[i].upper())
    else:
        cadena_reves.append(cadena_palabras[i].lower())

string = ""
for j in cadena_reves:
    string += j + " "

print(string)
