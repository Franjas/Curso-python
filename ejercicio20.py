#Crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if x % 2 == 0:
        return True

    return False

res1 = filter(mifuncion, numeros)


def suma(a, b):
    return a + b

res2 = reduce(suma, res1)
print(res2)