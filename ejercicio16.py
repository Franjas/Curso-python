#Crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora. En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
import time

ha = time.strftime('%H')  # hora actual
he = time.strftime('%M')  # hora especificada

#Trabajamos con condicionales:
if int(ha) >= 19:
    print('Hora de ir a casa')

else:
	print("Faltan {} horas y {} minutos".format(
	    18 - int(ha), 59-int(he)))