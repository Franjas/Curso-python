"""Crear la clase Vehículo la cual tendrá los siguientes atributos:

*Color

*Ruedas

*Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

*Velocidad

*Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola."""

class Vehículo:
    color = 'verde'
    ruedas = 4
    puertas = 4
    
class Coche(Vehículo):
    velocidad = 200
    cilindrada = 4

características = Coche
print('El vehículo tiene un motor de',características.cilindrada, 'cilindros,','con velocidad máxima de', características.velocidad, 'km/h,', características.puertas,'puertas, color', características.color)   