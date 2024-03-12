import random
from personaje import Personaje

print("¡Bienvenido a Gran Fantasía!")
jugador_nombre = input("Por favor indique nombre de su personaje: ")

jugador = Personaje(jugador_nombre)
print(jugador.estado)

orco = Personaje("Orco")
opcion = Personaje.enfrentamiento(orco, jugador)

while opcion == 1:
    resultado = "Ganado" if random.uniform(0, 1) <= jugador.probabilidad_ganar(orco) else "Perdido"
    if resultado == "Ganado":
        print(f"¡Le has {resultado} al orco, felicidades! ¡Recibirás 50 puntos de experiencia!")
        jugador.estado = 50
        orco.estado = -30
    else:
        print(f"¡Has perdido. El orco gana 50 puntos. ¡Pierdes 30 puntos!")
        jugador.estado = -30
        orco.estado = 50

    
    
    print(jugador.estado)
    print(orco.estado)

    opcion = Personaje.enfrentamiento(orco, jugador)

if opcion == 2:
    print("¡Has huido! El orco ha quedado atrás.")