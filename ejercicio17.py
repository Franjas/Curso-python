#Crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

file = open('preparados.txt', 'w') 
file.write('One\n')
file.write('Two\n')
file.write('Three\n')
file.close()
#Agregando nueva información a la existente:
file = open('preparados.txt', 'a')
file.write('GO!')
file.close()