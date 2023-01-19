

from jugador import Jugador
from supertopo import Supertopo

movimientoPlayer = ""
nombre = (input('Hola, ¿Cómo te llamas?: '))
jugador = Jugador(nombre, 1)

lista_topos = []

for i in range(4):
    supertopo = Supertopo()
    supertopo.__int__()
    lista_topos.append(supertopo)

while movimientoPlayer != 'stop' and int(jugador.get_casilla()) <= 30:
    movimientoPlayer = (input(nombre + ' , ¿Cúanto quieres avanzar, 1 o 2 pasos?: '))
    print(jugador.mover(int(movimientoPlayer)))
    for topo in lista_topos:
        print(supertopo.mover())

    if jugador.get_casilla() == supertopo.getSitio():
        print('Perdiste')
