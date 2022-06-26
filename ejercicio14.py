#crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
       def __init__(self):
           self.nombre = input('Ingrese el nombre del alumno:\n')
           self.nota = input('Nota del alumno:' )
           
       def imprimir(self):
            print('Alumno: ', self.nombre)
            print('Nota: ', self.nota)
            print('')
            
       def resultado(self):
        if float (self.nota) > 5:
            print('El alumno ha Aprobado')
                
        else:
            print('El alumno ha reprobado')
                
alumno1 = Alumno()

alumno1.imprimir()
alumno1.resultado()