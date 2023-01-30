from jugador import Jugador
from supertopo import Supertopo

# variables
movimientoPlayer = ""
cadena = "______________________________"
lista_topos = []
perder = False

nombre = input('Hola, ¿Cómo te llamas?: ')

# inicializamos jugador
jugador = Jugador(nombre, 1)

# inicializamos topos y agregamos a lista
for i in range(4):
    supertopo = Supertopo()
    supertopo.__int__()
    lista_topos.append(supertopo)

# colocamos jugador en grafico
y = list(cadena)
y[jugador.get_casilla() - 1] = 'X'
cadena = "".join(y)

# colocamos topos en graficos
for topo in lista_topos:
    y = list(cadena)
    y[topo.get_sitio()] = 'O'
    cadena = "".join(y)

# imprimimos grafico
print('Iniciamos¡¡¡' + cadena)

# condicion mientras jugador no llegue a meta o pierda:
while jugador.get_casilla() <= 30 and perder == False:

    try:
        movimientoPlayer = input(nombre + ' , ¿Cúanto quieres avanzar, 1 o 2 pasos?: ')
        cadena = "______________________________"
        if int(movimientoPlayer) == 1 or int(movimientoPlayer) == 2:
            print(jugador.mover(int(movimientoPlayer)))
            # jugador.mover(int(movimientoPlayer))
            l = list(cadena)
            l[jugador.get_casilla() - 1] = 'X'
            cadena = "".join(l)

            for topo in lista_topos:
                if 0 < topo.get_sitio() < 30:
                    print(topo.mover())
                    # topo.mover()
                    f = list(cadena)
                    f[topo.get_sitio() - 1] = 'O'
                    cadena = "".join(f)
                    # print(cadena)
                    if jugador.get_casilla() == topo.get_sitio():
                        t = list(cadena)
                        t[jugador.get_casilla() - 1] = 'T'
                        cadena = "".join(t)
                        print(cadena)
                        print('Perdiste')
                        perder = True
                        break
            if perder == False:
                print(cadena)
            cadena = "______________________________"
        else:
            print("Debe ser 1 o 2")
    except ValueError:
        if movimientoPlayer == 'stop':
            break
        else:
            print("Error, no es un número")
    except IndexError:
        if jugador.get_casilla()>=30:
            print('GANASTES¡¡¡')
            break
