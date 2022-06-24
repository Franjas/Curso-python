"""Crear la clase Vehículo la cual tendrá los siguientes atributos:

*Color

*Ruedas

*Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

*Velocidad

*Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola."""

class Vehiculo():

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cilindros".format(self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada)

coche = Coche("verde", 4, 4, 200, 4)
print(coche)  