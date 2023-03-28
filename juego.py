import random

def jugar(vidas):
    
    numero_random = int(random.randint(1,100))
    numero_elegido = None
    
    print()
    print('********* INICIO DEL JUEGO *********')
    print(f'Tienes {vidas} Vidas')
    print()
    
    while numero_random != numero_elegido:
        
        numero_elegido = int(input('Ingrese un numero entre 1 y 100: '))
        
        if numero_random > numero_elegido:
            print('Elige un número mayor')
            vidas -= 1
            
        elif numero_random < numero_elegido:
            print('Elige un número menor')
            vidas -= 1
            
        elif numero_elegido == numero_random:
            print()
            print('****** FELICIDADES GANASTE ******')
            break
              
        if vidas == 0:
            print()
            print('****** GAME OVER ******')
            print(f'EL numero elegido era el {numero_random}')
            break 
        
        print(f'******* Te quedan {vidas} vidas *******')
        print()

def main():
    while True:
        menu = '''
        ADIVINA EL NUMERO
        1 - Nivel Facil (10 vidas)
        2 - Nivel Intermedio (7 vidas)
        3 - Nivel DIficil (5 vidas)
        4 - Salir
        
        Ingresa Opcion: '''
        opcion = int(input(menu))
        
        if opcion == 1:
            jugar(10) 
        elif opcion == 2:
            jugar(7)
        elif opcion == 3:
            jugar(5)
        elif opcion == 4:
            print('Cerrando el juego')
            break    
        else:
            print('Eleje la opcion correcta')
             

if __name__ == '__main__':
    main()