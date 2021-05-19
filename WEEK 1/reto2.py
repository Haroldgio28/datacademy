'''Reto 2 - Piedra, papel o tijera
Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil. Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.

Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

Ejemplo:

ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2'''

import random
    
def ppt():
    contador1=0
    contador2=0 

    while True: 
        print('///////////')
        print('Marcador')
        print("Jugador 1: ",contador1)
        print("Jugador 2: ",contador2)
        p1=int(input('jugador 1-Introduce un número (1-piedra,2-papel,3-tijera): '))
        p2=int(random.randint(1,3))
        print('maquina: ',p2)
        
        
        if p1==p2:
            print('Empate')
            
        elif (p1==1 and p2==2) or (p1==2 and p2==3) or (p1==3 and p2==1):
            print('Gana maquina')
            contador2+=1
        else:
            print('Gana jugador 1')
            contador1+=1
            
        
        if contador1<2 and contador2<2:
            continue
        elif contador1==2:
            print('El jugador 1 gana')
            break
        elif contador2==2:
            print('La maquina gana la partida')
            break 

    print('-------------------------')
    print('Marcador Final:')
    print("Jugador 1: ",contador1)
    print("Jugador 2: ",contador2)


        
if __name__=='__main__':
    ppt()