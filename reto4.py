'''Reto 4 - Calculadora de volúmenes
Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen de un cilindro.

Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas en tu programa recibiendo datos como altura y radio.

Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.
'''

def run():
    tipocalculo=int(input('''
    De cual sólido quiere calcular el volumen:
    1-Cilindro
    2-Esfera
    3-Cubo
    4-Cono
    '''))

    if tipocalculo==1:
        radio=int(input('Ingrese el radio del cilindro: '))
        altura=int(input('Ingrese la altura del cilindro: '))
        cilindro(radio,altura)
    elif tipocalculo==2:
        radio=int(input('Ingrese el radio de la esfera: '))
        esfera(radio)
    elif tipocalculo==3:
        lado=int(input('Ingrese el lado del cubo: '))
        cubo(lado)
    elif tipocalculo==4:
        radio=int(input('Ingrese el radio del cono: '))
        altura=int(input('Ingrese la altura del cono: '))
        cono(radio, altura)
    else:
        print('Ingresó un valor incorrecto')
        quit


def cilindro(radio,altura):
    volumen=3.1416*(radio**2)*altura
    print('El volumen del cilindro indicado es de : ',volumen, 'unidades cubicas')

def esfera(radio):
    volumen=3.1416*(radio**3)*4/3
    print('El volumen de la esfera indicada es de : ',volumen, 'unidades cubicas')

def cubo(lado):
    volumen=lado**3
    print('El volumen del cubo indicado es de : ',volumen, 'unidades cubicas')

def cono(radio,altura):
    volumen=3.1416*(radio**2)*altura/3
    print('El volumen del cono indicado es de : ',volumen, 'unidades cubicas')

if __name__=='__main__':
    run()
