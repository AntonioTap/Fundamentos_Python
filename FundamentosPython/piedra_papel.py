# Eleccion de Maquina
import random

num_rand = random.randint(1,3)
if num_rand == 1:
    choice_maq= 'Piedra'

elif num_rand == 2:
    num_rand = 'Papel'
else:
    choice_maq = 'Tijeras'
# Eleccion de Usuario
choice_text = '''
Escribe una Opcion
    Piedra
    Papel
    Tijeras 
'''
choice_user = input(choice_text)
# Imprime seleccion
print ("Usuarios elige: ", choice_user)
print ("Maquina elige: ", choice_maq)
# Define Ganador 
if choice_user == choice_maq:
    print("Es un empate")
else:
    if choice_user == 'Piedra' and choice_maq == 'Papel':
        print("Gana la Maquina")
    elif choice_user == 'Piedra' and choice_maq == 'Tijeras':
        print("Gana Usuario")
    elif choice_user == 'Papel' and choice_maq == 'Piedra':
        print("Gano Usuario")
    elif choice_user == 'Papel' and choice_maq == 'Tijeras':
        print("Gano Maquina")
    elif choice_user == 'Tijeras' and choice_maq == 'Piedra':
        print("Gano Maquina")
    else:
        print("Gano Usuario")
       