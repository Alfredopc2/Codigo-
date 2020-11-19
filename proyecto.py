import random

print('¡Hola!, en este juego tratarás de conseguir un objeto extraordinariamente raro. ¡Suerte, la necesitarás!')
print('Para empezar a jugar, ingresa tu nombre.')
miNombre = input()
print('Muy bien, ' + miNombre + ', aquí tienes tu llave.')

print('¿Quieres abrir una caja? ' + 'Presiona 1 para abrirla, presiona 2 para no abrirla.')
confirmacion = input()
confirmacion = int(confirmacion)

roll = random.randint(1,10000)

while confirmacion == 1:
    input()
    print('Abriendo caja...')

    if roll <= 7992:
        print('azul')




        
    

    
