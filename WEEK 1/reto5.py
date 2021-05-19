''' Reto 5 - Rangos cambiantes
Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: un límite inferior, un límite superior y uno de comparación.

Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.

En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y pide ingresar otro número para repetir el proceso.
'''

def run():
    liminf=int(input("Ingresa el límite inferior: "))
    limsup=int(input("Ingresa el límite superior: "))
    comparat=int(input('Ingresar el número a comparar: '))

    if liminf>limsup:
        print('El límite inferior es mayor que el límite superior, por favor ingrese de nuevo los límites.')
        liminf=int(input("Ingresa el límite inferior: "))
        limsup=int(input("Ingresa el límite superior: "))
          

    while True:
        
        if comparat<liminf or comparat>limsup:
            print('El número ', comparat,' está fuera de los límites indicados')
            comparat=int(input('Ingrese un número dentro de los límites: '))
            continue
        else:
            print('El número ', comparat, ' está en los límites indicados')
            break

if __name__=='__main__':
    run()