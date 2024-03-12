
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado (self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    @estado.setter
    def estado (self, experiencia):
        tempexp = self.experiencia + experiencia
        if tempexp >= 0:
            self.experiencia = tempexp
            self.nivel = tempexp // 100 + 1 if tempexp >= 0 else 1

    def __lt__(self, other):
        return self.nivel < other.nivel

    def __gt__(self, other):
        return self.nivel > other.nivel

    def probabilidad_ganar(self, otro_personaje):
        if self < otro_personaje:
            return 0.33
        elif self > otro_personaje:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def enfrentamiento(orco, jugador):
        probabilidad = jugador.probabilidad_ganar(orco)
        print(f"¡Oh no!, ¡Ha aparecido un Orco! Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30. Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = int(input("¿Qué deseas hacer? 1. Atacar 2. Huir: "))
        return opcion