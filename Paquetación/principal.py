## Aquí se pondrán los módulos y paquetes
import modulo as m1
import funciones_principales.main_funciones as fp
from funciones_principales.funciones_secundarias.secondary_funciones import multiplicacion


a = 5
b = 4

print(a+b)

print(m1.suma(a, b))
print(fp.resta(a, b))
print(multiplicacion(a, b))