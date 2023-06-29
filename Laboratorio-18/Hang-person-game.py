import random
import time

total_user = 0
adivinaste = 0 
palabrasingular = 0
perdiste = 0
user_option = ""
letra_usuario = []
palabra = "gato"
intentos = 5
nombre = input ("¿Cual es tu nombre? \n\n")     
print (f"¡¡Holaaa {nombre}!! ¡Vamos a jugar! \n \n")


AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
while (user_option != 3):
    print  (f"[------ Juego del AHORCADO ------] \n \n"
            f"1. Jugar \n"
            f"2. Mostrar resultados \n"
            f"3. Salir\n")
    user_option = int (input())

    if user_option == 1 :
        print ("¡Vamos a Jugar")
        print (f"Jugador : {nombre}")
        
        if len(palabra) == 0:
          print ("¡Felicidades! ¡La adivinaste!")
                 
            
        else:
                print (f"Te quedan {len (palabra)} palabras por adivinar.")
                palabra_mostrada = random.choice(palabra)
                intentos = 6
                letras_adivinadas = []
        
        letra = input ("Ingrese una Letra: \n \n")
    if (letra in palabra):
        print ("adivinaste la letra \n")
        
        for letra in palabra:
            print (letra)
            if (letra == letra_usuario ):
                palabra_mostrada += letra_usuario
            else: 
                palabra_mostrada += "_ "
                palabra_mostrada = "_ " * len (palabra)
        print (palabra_mostrada)   
        

    else:
        print ("no adivinaste")

    