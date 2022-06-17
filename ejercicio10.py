"""Escribe una función que calcule el área de un triángulo, recibiendo la altura 
y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo."""

def area_triángulo(base=6, altura=10):
    return(base * altura) / 2

def area_circulo(r=6, pi=3.1415):
    return pi * (r**2)
    

resultado1 = area_triángulo(base=6, altura=10)
resultado2 = area_circulo(r=6, pi=3.1415)
print('El area del Triángulo es:',resultado1,'cm y el area del Circulo es:', resultado2,'metros^')
