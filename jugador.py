
class Jugador:
    nombre = ""
    casilla = 0

    def __init__(self, nombre, casilla):
        self.nombre = nombre
        self.casilla = casilla

    def mover(self, casilla):
        self.casilla = self.casilla + casilla
        return self.casilla

    def get_casilla(self):
        return self.casilla