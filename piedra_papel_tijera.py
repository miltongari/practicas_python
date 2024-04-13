import random


class JuegoPPT:

    def __init__(self):
        self.opcion = ["piedra", "papel", "tijera"]

    def jugar(self):
        elecion_jugador = input("Elige:\n piedra\n papel\n tijera\n").lower()
        elecion_computadora = random.choice(self.opcion)
        print("La computadora elige: {}".format(elecion_computadora))

        if elecion_jugador not in self.opcion:
            print("Elecion invalidad")

        elif (
            (elecion_jugador == "piedra" and elecion_computadora == "tijera")
            or (elecion_jugador == "papel" and elecion_computadora == "piedra")
            or (elecion_jugador == "tijera" and elecion_computadora == "papel")
        ):
            print("Ganaste")

        elif elecion_jugador == elecion_computadora:
            print("Empate")

        else:
            print("Perdiste")


juego = JuegoPPT()
juego.jugar()
