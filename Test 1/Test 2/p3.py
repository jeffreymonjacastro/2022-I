#Funciones - Coprimos

num = int(input("Ingrese su número: "))

while num <= 1:
    num = int(input("Ingrese su número: "))

def coprimos(n):
    cadena_coprimos = ""

    divisores = ""

    for i in range(2, n):
        result = True

        if n % i == 0:
            divisores += str(i)

        for j in range(2, i):

            if i % j == 0:
                result = False

        if result:
            cadena_coprimos += str(i) + " "

    return cadena_coprimos


print(f"Los numeros coprimos y menores a {num} son:")
print(coprimos(num))