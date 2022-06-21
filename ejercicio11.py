#Escribe una función que pueda decirte si un número (número entero) es primo o no:

def es_primo(número):
    if número <= 1:
        return False
    
    elif número == 2:
        return True
    
    else:
        for i in range(2, número):
            if número % i == 0:
                return False #el número es compuesto.
        
        return True #el número es primo.


"""for i in range(1, 101):
    print(i, es_primo(i))"""
print(es_primo(7)) #Acá podemos usar cualquier número en específico. En este caso se usó el 7. Con la nota anterior, se imprime el rango entre 1 y 100.