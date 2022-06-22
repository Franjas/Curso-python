#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no:

año = int(input('Por favor, ingrese el año a consultar:\n'))

def bisiesto(año):
    if año % 4 == 0 and año % 100 != 0:
        return True
    
    elif año % 100 == 0 and año % 400 == 0:
        return True
    else:
        False
        
print(bisiesto(año))