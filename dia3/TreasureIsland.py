print("Bievenido a la ISLA DEL TESORO\n"
      "Tu misión será encontrar el tesoro")
print("Estás en una encrucijada:"
      "¿Qué Camino quieres tomar?:")
camino=input("Izquierda o Derecha:").strip().upper()
if camino=="DERECHA":
    print("Has encontrado un lago!!")
    espera=input("Quieres esperar o nadar al otro lado? ESPERAR | NADAR").strip().upper()
    if espera=="ESPERAR":
        print("Has encontrado un bote puedes seguir!!")
        puerta=input("Has encontrado tres puertas, AZUL, ROJO, AMARILLO , ELIGE").strip().upper()
        if(puerta=="AMARILLO"):
            print("Has ganado el juego el tesoro es tuyo!!")
        elif(puerta=="ROJO"):
            print("Has sido quemado por lava, FIN DEL JUEGO!!")
        elif(puerta=="AZUL"):
            print("Has sido atacado por bestias, FIN DEL JUEGO!!")
        else:
            print("Has sido atrapado por una trampa!! FIN DEL JUEGO")
    else:
        print("Has sido atacado por un tiburón!! FIN DEL JUEGO")


else:
    print("Has caído en un hoyo y muerto!!"
          "FIN DEL JUEGO ")
