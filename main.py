from jugador import Jugador
from supertopo import Supertopo

# variables
movimientoPlayer = ""
cadena = "______________________________"
lista_topos = []
perder = False

nombre = input('Hola¡, Bienvenido a TOPOLLÍN. Tendrás que llegar a la casilla 30 sin toparte con ningún topo.'
               'Cuando quieras terminar de jugar escriba STOP. Empecemos¡¡¡¡\n¿Cómo te llamas?: ')

# inicializamos jugador
jugador = Jugador(nombre, 1)

# inicializamos topos y agregamos a lista
for i in range(4):
    supertopo = Supertopo(10, 20)
    lista_topos.append(supertopo)

# colocamos jugador en grafico
y = list(cadena)
y[jugador.get_sitio() - 1] = 'J'
cadena = "".join(y)

# colocamos topos en graficos
for topo in lista_topos:
    y = list(cadena)
    y[topo.get_sitio()] = 'T'
    cadena = "".join(y)

# imprimimos grafico
# print(jugador.get_sitio())
# for topo in lista_topos:
#    print(topo.get_sitio())
print('Iniciamos¡¡¡ ' + cadena)

# condicion mientras jugador no llegue a meta o pierda:
while jugador.get_sitio() <= 30 and perder == False:

    # cubre el caso en el que se introduzca texto y no sea stop, si es stop saldra del programa, trata dos excepciones
    try:
        movimientoPlayer = input(nombre + ' , ¿Cúanto quieres avanzar, 1 o 2 pasos?: ')
        cadena = "______________________________"
        # comparamos si los numero metidos son 1 o 2
        if int(movimientoPlayer) == 1 or int(movimientoPlayer) == 2:
            # en el caso q sean 1 o 2 movera el jugador
            # print('jugador' + jugador.mover(int(movimientoPlayer)))
            jugador.mover(int(movimientoPlayer))
            l = list(cadena)
            l[jugador.get_sitio() - 1] = 'J'
            cadena = "".join(l)

            # aqui movemos a los tops
            for topo in lista_topos:
                # si los topos estan entre 0 y 30 se imprimen
                if 0 < topo.get_sitio() < 30:
                    # print('Topo' + topo.mover())
                    topo.mover()
                    f = list(cadena)
                    f[topo.get_sitio() - 1] = 'T'
                    cadena = "".join(f)
                    # print(cadena)
                    # en el caso que el jugador y un topo esten en el mismo puesto se termina la partida y muestra donde muere
                    if jugador.get_sitio() == topo.get_sitio():
                        t = list(cadena)
                        t[jugador.get_sitio() - 1] = 'P'
                        cadena = "".join(t)
                        print(cadena)
                        print('Perdiste')
                        perder = True
                        break
            # si no pierde imprime la cadena y despues la resetea
            if perder == False:
                print(cadena)
            cadena = "______________________________"
        else:
            print("Debe ser 1 o 2")
    except ValueError:
        if movimientoPlayer.lower() == 'stop':
            break
        else:
            print("Error, no es un número")
    except IndexError:
        if jugador.get_sitio() >= 30:
            print('GANASTES¡¡¡')
            break
