#Cadenas - Contador de palabras

frase = input("Ingrese la frase:")
palabra = input("Ingrese la palabra a contar:")

for letra in frase:
    if letra == " ":
        palabras = frase.split()
    elif letra == ",":
        palabras = frase.split(sep=",")

for i in palabras:
    count = 0
    if i == palabra:
        count += 1

print("El numero de veces que aparece la palabra es:", count)

