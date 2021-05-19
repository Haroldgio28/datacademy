'''
Reto 3 - Conversor de millas a kilómetros
Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. Para no estar repitiendo este cálculo escribe un programa en que el usuario indique una cantidad de millas y en pantalla se muestre el resultado convertido a kilómetros.

Toma en cuenta que en cada milla hay 1.609344 Km

Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.
'''

def run():
    tipoconv=int(input('''
    1- Km a millas
    2- millas a km
    '''))
    
    valor=int(input("Insertar valor a convertir: "))

    if tipoconv==1:
        kmmill(valor)
    elif tipoconv==2:
        millkm(valor)
    else:
        print('Ingresó un valor incorrecto')
        quit

    
def kmmill(valor):
    # valor=int(input("Insertar valor a convertir: "))
    conv= valor/1.609344
    print (valor,' kms equivalen a ',conv,' millas')

def millkm(valor):
    # valor=int(input("Insertar valor a convertir: "))
    conv= valor*1.609344
    print (valor,' millas equivalen a ',conv,' kms')



if __name__=='__main__': 
    run()