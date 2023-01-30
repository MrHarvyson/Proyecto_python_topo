import random

class Supertopo:
    casilla = 0
    direcion = 1

    # inicializa a los topos
    def __init__(self, ini, fin):
        self.casilla = random.randint(ini, fin)

    # mueve a los topos
    def mover(self):
        random_numero = random.randint(1, 3)
        self.direcion = random.randint(1, 2)
        if self.direcion == 1:
            self.casilla = self.casilla - random_numero
        else:
            self.casilla = self.casilla + random_numero

        return self.casilla

    # devuelve la posicion de los topos
    def get_sitio(self):
        return self.casilla


