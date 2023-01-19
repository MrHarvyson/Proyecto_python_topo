import random

class Supertopo:
    casilla = 0
    direcion = 1

    def __int__(self):
        self.casilla = random.randint(10, 20)

    def mover(self):
        random_numero = random.randint(1, 3)
        self.direcion = random.randint(1, 2)
        if self.direcion == 1:
            self.casilla = self.casilla - random_numero
        else:
            self.casilla = self.casilla + random_numero

        return self.casilla

    def getSitio(self):
        return self.casilla
