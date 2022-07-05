#Crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo():

    def __init__(self, color, modelo, puertas, marca):
        self.color = color
        self.molelo = modelo
        self.puertas = puertas
        self.marca = marca
        self.estado = False
        
    def encender(self):
        if not self.estado:
            self.estado = True
        
    def apagar(self):
        if not self.estado:
            self.estado = False
        
    def acelerar(self):
        if self.estado:
            print('El vehículo ha acelerado')
        
    def frenar(self):
        if self.estado:
            print('El vehículo a frenado')
        
        
f = open('clssVehiculo.bin', 'rb')
coche = pickle.load(f)
f.close()