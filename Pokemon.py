import random
import time 

adivinaste = 0
palabra_singular = "palabra"
perdiste = 0
user_option = ""
palabras = ["pikachu","charmander","bulbasaur","squirtle","psyduck"]
jugador = "" 

nombre = input ("¿Cual es tu nombre? \n\n")     
print (f"¡¡Holaaa {nombre}!! ¡Vamos a jugar! \n \n")   
    

while (user_option != 4): 
    print ("[------ ¡¡¡El Juego de los Pokémon!!! ¿Pika-Pika? Pikachuuu ------]\n")
    print ("1. Quiero jugar 🕹️ \n") 
    print ("2. Quiero saber los resultados \n" ) 
    print ("3. Datos Curiosos \n") 
    print ("4. Salir \n")     
    user_option = int (input())
    
    if (user_option == 1) :
            #¡opción si el usuario adivino todas las palabras!
            if len(palabras) == 0:
                print("     __^__                     __^__  ")
                print("    ( ___ )-------------------( ___ ) ")
                print("     | / |   ¡Felicidades!     | / |  ")
                print("     | / |     Le acertaste    | / |  ")
                print("     |___|           a todas.  |___|  ")
                print("    (_____)-------------------(_____) ")
            
            else:
                print (f"Te quedan {len (palabras)} palabras por adivinar.")
                palabra_secreta = random.choice(palabras)
                intentos = 6
                letras_adivinadas = []
                print ("¡Vamos a jugar \n!")
                print (f"Jugador: {nombre}\n")

                print ("______________________________")

                print ("⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜")
                print ("⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥⬛⬜⬜")
                print ("⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜")
                print ("⬜⬛⬛⬜🟥🟥🟥🟥🟥🟥🟥⬛⬜")
                print ("⬛⬜⬜⬜⬜🟥🟥🟥🟥🟥⬛⬛⬛")
                print ("⬜⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛⬛")
                print ("⬜⬜⬛🟨⬛🟨🟨⬛⬛⬛⬛⬛⬛")
                print ("⬜⬜⬛🟨⬛🟨🟨⬛🟨🟨⬛⬛⬜")
                print ("⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜")
                print ("⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛🟦⬛⬜")
                print ("⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛🟦⬛⬜")
                print ("⬜⬜⬛⬛⬛⬛⬛⬛🟨🟨⬛⬛⬜")
                print ("⬜⬛⬜⬜⬛⬜⬜⬛🟨🟨⬛⬜⬛")
                print ("⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜⬛")
                print ("⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬛⬜")
                print ("________________________________")
                print ("Lanzando la ¡Pokebola! . . .\n\n")
                time.sleep(1)        
                print ("________________________________")
                time.sleep (0.3)
                print  (   "⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜") 
                print (    "⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜") 
                print (    "⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜") 
                print (    "⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜") 
                print (    "⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜") 
                print (    "⬛🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥⬛") 
                print (    "⬛🟥🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥🟥⬛") 
                print (    "⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛") 
                print (    "⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛") 
                print (    "⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜") 
                print (    "⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜") 
                print (    "⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜") 
                print (    "⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜") 
                print (    "⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜")

                print ("__________________________________")

                print("¡Adivina que pokémon es! ¡Tienes 3 intentos! ¡Wuajajaja! ")
                
                if len(palabras) == 0:
                    print ("「")
                    print ("¡Felicidades! ¡Adivinaste que pokémon hemos capturado!  ")
                    print ("」")
                
                else:
                    print (f"Te quedan {len (palabras)} palabras por adivinar.")
                    palabra_secreta = random.choice(palabras)
                    intentos = 3
                    palabras_adivinadas = []

                    
                    if(palabra_secreta == "pikachu"):
                        print ("⌜                                         ⌝")
                        print (" Soy un Pokémon de tipo eléctrico, Tengo   ")
                        print (" las mejillas rojas y la cola en forma de  ")
                        print (" rayo. Soy el compañero fiel de Ash        ")
                        print (" Ketchum y mi nombre suena como una chispa ")
                        print ("¿Qué Pokémon soy?                          ")
                        print ("⌞                                         ⌟")

                    elif(palabra_secreta == "charmander"):
                        print ("⌜                                         ⌝")
                        print (" Soy un Pokémon de tipo fuego, Tengo la    ")
                        print (" piel naranja y la cola con una llama. Soy ")
                        print (" el inicial favorito de muchos entrenadores")
                        print (" Y mi nombre suena como un encendedor      ")
                        print ("¿Qué Pokémon soy?                               ")
                        print ("⌞                                         ⌟")
                    
                    elif(palabra_secreta == "bulbasaur"):
                        print ("⌜                                         ⌝")
                        print (" Soy un Pokémon de tipo planta, Tengo una  ")
                        print (" semilla en el lomo, Tengo la piel verde y ")
                        print (" las orejas puntiagudas. Soy el primero de ")
                        print (" la Pokédex Nacional Y mi nombre suena como")
                        print (" una bombilla rara                         ")
                        print ("¿Qué Pokémon soy!                                ")
                        print ("⌞                                         ⌟")

                    elif(palabra_secreta == "squirtle"):
                        print("Soy una tortuga azul que lanza agua, Me     ")
                        print("escondo en mi caparazón cuando hay batalla. ")
                        print("¿Qué Pokémon soy?                          ")
                        print("____________________________________________________________________________________|")
                    
                    elif(palabra_secreta == "psyduck"):
                        print("Soy un pato amarillo que tiene jaqueca,     ")
                        print("Cuando me duele mucho, uso telequinesis")
                        print("¿Qué Pokémon soy?")

                        
                    print("_ " * len(palabra_secreta))

                    while True:

                        palabra_usuario = input("Ingresa la palabra: ").lower().strip()

                        if palabra_usuario == "":
                            continue
                        
                        if palabra_usuario in palabras_adivinadas:
                            print("Ya has adivinado la palabra.")
                            continue

                        if palabra_usuario in palabra_secreta:
                            palabras_adivinadas.append(palabra_usuario)
                            print("¡Correcto!")
                        
                        else:
                            intentos -= 1
                            print("Incorrecto.")
                            print(f"Te quedan {intentos} intentos.")
                        
                        if len(palabras_adivinadas) == 0:
                            continue
                    
                        if intentos == 0:
                            print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")
                            perdiste = perdiste + 1
                            break

                        palabra_secreta_intento = ""
                        
                        for palabra in palabra_secreta:
                            if palabra in palabras_adivinadas or palabra == " ":
                                palabra_secreta_intento += palabra
                                print(f"{palabra} ", end= "")
                            else:
                                palabra_secreta_intento += "_"
                                print(f"_ ", end= "")

                        print("\n\n")

                        if palabra_secreta_intento == palabra_secreta or palabra_usuario == palabra_secreta :
                            print("¡Felicidades! ¡Has ganado!")
                            adivinaste = adivinaste + 1
                            palabras.remove(palabra_secreta)

                            print ("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥") 
                            print ("¡Pokémon yo te elijo!")
                            time.sleep(3)

                            print ("___________________________________")
                            time.sleep(0.3)
                            print      (  "    ⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀ ")
                            print      (   "⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀")
                            print      (   "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀")
                            print      (   "⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠙⣿⣿⣿⣿⣿⣆⠀")
                            print      (   "⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣧⡀⠀⢠⣿⠟⠛⠛⠿⣿⡆")
                            print      (   "⠀⢰⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠙⠿⠿⠟⠋⠀⠀⠀⣠⣿⠇")
                            print      (   "⠀⢸⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠋⠀")
                            print      (   "⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣾⠿⠛⠉⠀⠀⠀⠀")
                            print      (   "⠀⠈⢿⣷⣤⣤⣄⣠⣤⣤⣤⣤⣶⣶⣾⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀")
                            print      (   "⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀")
                            print      (   "⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀")
                            print      (   "⠀⢸⣿⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀")
                            print      (   "⠀⠀⢻⣧⠀⠈⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
                            print      (   "⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁")
                            print      (   "⠀⠀⠀⠀⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠟⠀⣠⣾⠟⠀⠀")
                            print      (   "⠀⠀⠀⠀⠀⠈⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢀⣤⣾⠟⠁⠀⠀⠀")
                            print      (   "⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣶⣦⣤⣤⣤⣤⣤⣤⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀")
                            print      (   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            time.sleep (0.2)
                        
                            if (palabra_secreta == "pikachu"): 
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛💛")
                                    print ("⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛💛💛")
                                    print ("💛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛💛💛💛")
                                    print ("💛💛⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛💛💛💛💛")
                                    print ("💛💛💛⬛⬛⬛💛💛💛💛💛💛💛⬛⬛⬛💛💛💛💛💛")
                                    print ("💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
                                    print ("💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛⬛")
                                    print ("💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛⬛💛")
                                    print ("⬛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛⬛⬛💛💛")
                                    print ("💛💛💛⬛💛💛💛💛💛💛💛💛💛💛⬛💛💛⬛💛💛⬛")
                                    print ("💛💛⬛⬜⬛💛💛💛💛💛💛💛💛⬛⬜⬛💛⬛⬛⬛⬜")
                                    print ("💛💛⬛⬛⬛💛💛💛💛💛💛💛💛⬛⬛⬛💛⬛⬜⬜⬜")
                                    print ("💛💛⬛⬛⬛💛💛💛💛⬛💛💛💛⬛⬛⬛💛💛⬛⬜⬜")
                                    print ("⬛⬛💛💛💛💛💛💛💛💛💛💛💛💛💛💛⬛⬛⬛⬜⬜")
                                    print ("🍎🍎⬛💛💛⬛⬛⬛⬛⬛⬛⬛💛💛💛💛🍎🍎⬛⬛⬛")
                                    print ("🍎🍎⬛💛💛💛⬛⬛⬜⬜⬛⬛💛💛💛⬛🍎🍎⬛💛💛")
                                    print ("🍎🍎⬛💛💛💛⬛⬜⬜⬜⬜⬛💛💛💛⬛🍎🍎⬛💛💛")
                                    print ("⬛⬛💛💛💛💛💛⬛⬜⬜⬜⬛💛💛💛⬛⬛⬛💛💛💛")
                                    print ("💛💛💛💛💛💛💛💛⬛⬛⬛💛💛💛💛💛💛⬛💛💛💛")
                            
                            elif (palabra_secreta == "charmander"):
                                    print ("⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜🟥⬜⬜")
                                    print ("⬜⬛🟦🟧🟧🟧🟧🟦⬛⬜⬜🟥🟥🟥⬜")
                                    print ("⬛⬜🟦🟧🟧🟧🟧🟦⬜⬛⬜🟥🟥🟥⬜")
                                    print ("⬛⬜🟦🟧🟧🟧🟧🟦⬜⬛🟥🟥🟨🟥⬜")
                                    print ("⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛🟥🟨🟨🟥🟥")
                                    print ("⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬛🟨🟥🟥")
                                    print ("⬛🟧⬛⬛⬛⬛⬛⬛🟧⬛⬜⬛🟧⬛⬜")
                                    print ("⬛🟧⬛🟧🟧🟧🟧⬛🟧⬛⬛🟧🟧⬛⬜")
                                    print ("⬜⬛🟧🟧🏻🏻🟧🟧⬛🟧🟧🟧⬛⬜⬜")
                                    print ("⬜⬛🟧🏻🏻🏻🏻🟧⬛🟧🟧🟧⬛⬜⬜")
                                    print ("⬜⬛🟧🏻🏻🏻🏻🟧⬛🟧⬛⬛⬜⬜⬜")
                                    print ("⬛🟧⬛⬛⬛⬛⬛⬛🟧⬛⬜⬜⬜⬜⬜")
                                    print ("⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜")
                            
                            elif (palabra_secreta == "bulbasaur"):
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜") 
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩⬛⬛⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩⬛⬛⬛⬛🟩🟩🟩⬛🟩⬛")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛🟩⬛")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛")
                                    print ("⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩🟩⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛")
                                    print ("⬜⬜🟦🟦🟦⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩⬛🟩")
                                    print ("⬜⬜🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩⬛🟩")
                                    print ("⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛") 
                                    print ("⬜⬜🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩⬛") 
                                    print ("⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩") 
                                    print ("⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩")
                                    print ("⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🌫️🌫️⬛🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩") 
                                    print ("⬜⬛🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟥🟥⬜🌫️⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩")
                                    print ("⬜⬛🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟥🟥⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩⬛")
                                    print ("⬛🌫️🟥⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥⬜🟥🟥⬜🌫️🟦🟦🟦⬛🟦⬛🟩🟩🟩🟩⬛") 
                                    print ("⬛⬜🟥⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥⬜🟥🟥⬜🌫️🟦🟦🟦⬛🟦🟦⬛🟩🟩⬛🟩")
                                    print ("⬛🟦🟥🟥🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥🟥🟥🌫️🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟩  ")
                                    print ("⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩")
                                    print ("⬛🟦⬛⬛🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛🟦🟦⬛🟦🟦🟦⬛⬛🟦🟦⬛")
                                    print ("⬜⬛🟦⬜🟥🟥🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬜⬛🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛⬛🟦🟦")
                                    print ("⬜⬜⬛🟦🟦⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦⬛⬛🟦🟦")
                                    print ("⬜⬜⬜⬛⬛🟦🟦⬛🟥🟥🟥🟥🟥🟥⬛🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦")
                                    print ("⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦⬛🟦🟦⬛🟦🟦🟦⬛🟦")
                                    print ("⬜⬜⬜⬜⬜⬛🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦⬛🟦🟦⬛⬛⬛")


                            elif (palabra_secreta == "squirtle"):
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜")
                                    print ("⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜")
                                    print ("⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦")
                                    print ("⬜⬜⬜⬜⬜🟦🟫🟦🟦🟦🟦🟦🟦🟦🟦⬛🌫️🌫️🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜⬜🟦⬜🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🌫️🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜⬜🟦🟫🟦🟦🟦🟦🟦🟦🟦⬛⬛🟫⬜🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜⬜🟦⬛🟦🟦🟦🟦🟦🟦🟦⬜⬛🟫⬜🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟫⬛🟫⬜🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛")
                                    print ("⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜")
                                    print ("⬜🟦⬜🟦⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟫🟫🟦🟦🟦🟦⬜")
                                    print ("⬜🟦🟦🟦🟦⬛⬛🟦⬛⬛🟫🟧🟧🟧🟧🟫🟫🟦🟦🟦⬛🟦🟦")
                                    print ("🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟫🟫🟫🟫🟫🟦🟦🟦🟦  ⬜⬜⬜")
                                    print ("⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛🟧🌫️🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜")
                                    print ("⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟧🟧🟧🟦🟦🟦🟦")
                                    print ("⬜⬜🟦🟦🟦🟦🟦🟦🟦🟧🟧🏻🏻🏻🏻🟧🟧🟧🟦🟦🟦🟦🟦")
                                    print ("⬜⬜⬜🟦🟦🟦🟦🟦🟧🟧🏻🏻🏻🏻🟧🟧🟧🟧🟦🟦🟦🟦🟦")

                            
                            elif (palabra_secreta == "psyduck"):
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬜⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜")
                                    print ("⬜⬛🟨🟨⬛⬛🟨🟨🟨🟨⬛⬛⬜⬜⬜⬜⬜⬜")
                                    print ("⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜")
                                    print ("⬛🟨🏽⬜🏽🟨🟨🟨🏽🏽🟨🟨🟨⬛⬜⬜⬜⬜")
                                    print ("⬛🏽⬜⬛🏽🟨🟨🏽⬜⬜🏽🟨⬛🟨⬛⬜⬜⬜")
                                    print ("⬜⬛🏽⬜⬛⬛🏽⬜⬛⬜⬜⬛🟨🟨🟨⬛⬜⬜")
                                    print ("⬜⬛🟨⬛🟧🟧⬛⬛⬜⬜🏽⬛🟨🟨🟨⬛⬜⬜")
                                    print ("⬜⬛⬛🟧🟧⬛🟧🟧⬛🏽🟨⬛🟨🟨🟨🟨⬛⬜")
                                    print ("⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛🟨⬛🟨🟨🟨🟨⬛⬜")
                                    print ("⬛🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛🟨🟨🟨🟨⬛⬜⬜")
                                    print ("⬜⬛🟧🟧🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜")
                                    print ("⬜⬜⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬜")
                                    print ("⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨⬛")
                                    print ("⬜⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨⬛⬜")
                                    print ("⬜⬛⬜🟧⬛⬛🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛⬜⬜")
                                    print ("⬜⬜⬛⬛⬜🟧⬛⬛⬛⬛⬛🟧⬜⬛⬜⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬛⬛⬜⬛🟧⬜🟧⬜⬛⬜⬜⬜⬜⬜")
                                    print ("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜")
                
                            break
        
        
    elif ( user_option == 2):
            print("Cargando resultados...💣")
            time.sleep(1.5)
            print("3 ... 2 ... 1 ...")
            time.sleep(0.5)
            if adivinaste > 1:
                 palabra_plural = palabra_singular +"s"
            else:
                 palabra_plural = palabra_singular
            print(f"¡Le Atinaste! Has atrapado el Pokémon: {adivinaste} {palabra_plural}")
            print(f"No lo conseguiste, se no escapo el Pokémon: {perdiste} veces.\n")
            
            input ("presiona enter para continuar Jugando:") 
            time.sleep(1)
    
    elif (user_option == 3): 
         print ("Sabias que hay 1015 Pokémon registrados en la Pokedex")
    elif (user_option == 4):
        print("¡Gracias por jugar!")
        print("✨🌟💖💎🦄💎💖🌟✨🌟💖💎🦄💎💖🌟✨")
else:
        print("¡¡¡TE EQUIVOCASTE TONTO ENTRENADOR DE POKÉMON!!!🦗")