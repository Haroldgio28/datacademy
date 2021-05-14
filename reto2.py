'''Reto 2 - Piedra, papel o tijera
Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil. Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el jugador 1 o el jugador 2.

Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.

Ejemplo:

ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2'''

def run():
    
    p1=int(input('jugador 1-Introduce un número (1-piedra,2-papel,3-tijera): '))
    p2=int(input('jugador 2-Introduce un número (1-piedra,2-papel,3-tijera): '))
    ppt(p1,p2)
    

    
def ppt(p1,p2):
    contador1=0
    contador2=0
    if p1==p2:
        print('Empate')
    elif (p1==1 and p2==2) or (p1==2 and p2==3) or (p1==3 and p2==1):
        print('Gana jugador 2')
        contador2=+1
    else:
        print('Gana jugador 1')
        contador1=+1
    print(contador1,contador2)

if __name__=='__main__':
    run()