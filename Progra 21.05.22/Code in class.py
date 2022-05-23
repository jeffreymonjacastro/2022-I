DATA = [
    ["Alumno", "PC1", "PC2", "Asistencia", "Distrito"],
    ["David", 15,16, True, "San Borja"],
    ["Randy", 20,18, True, "Callao"],
    ["Dante", 18,19, False, "Canta"],
    ["Andre", 18,10, True, "Canta"]
]

# print(DATA[3][3])
#
# for i in range(5):
#     print(DATA[i][0])
#
# for i in range(5):
#     print(DATA[1][i], end=" ")

for i in range(5):
    for j in range(5):
        print(DATA[i][j], end="\t\t")
    print()

print("##########################")

for i in range(5):
    print(DATA[i][0],"\t",DATA[i][1],"\t",DATA[i][2],"\t",DATA[i][3],"\t",DATA[i][4])

print("##########################")

for i in range(5):
    for j in range(5):
        print('{:>7}'.format(DATA[i][j]), end="\t\t")
    print()

print("hello")

print("Estoy editando en una nueva rama")