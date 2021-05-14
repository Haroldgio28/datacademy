'''Reto 1: Área de un triangulo
El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 . Escribe un programa que tome la base y la altura como parámetros y calcule el área del triángulo.
Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno.'''


def run():
    base=int(input('intoduce la longitud de la base: '))
    altura=int(input('intoduce la longitud de la altura: '))
    lado1=int(input('introduce la longitud del lado 1 (diferente a la base): '))
    lado2=int(input('introduce la longitud del lado 2 (diferente a la base): '))
    area=str(((base*altura)/2))
    print('El área del triángulo dado es: '+ area +' unidades cuadradas')
    tipotriangulo(base,lado1,lado2)

def tipotriangulo(base, lado1, lado2):
    if base==lado1 and lado1==lado2:
        print('El triangulo es equilatero')
    elif base==lado1 or lado1==lado2 or base==lado2:
        print('El triangulo es isósceles')
    else:
        print('El triangulo es escaleno')


if __name__=='__main__':
    run()