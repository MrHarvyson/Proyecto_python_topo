
class Jugador:
    nombre = ""
    casilla = 0

    # inicializa el jugador
    def __init__(self, nombre, casilla):
        self.nombre = nombre
        self.casilla = casilla

    # mueve de casilla
    def mover(self, casilla):
        self.casilla = self.casilla + casilla
        return self.casilla

    # devuelve la casilla en la que esta
    def get_sitio(self):
        return self.casilla