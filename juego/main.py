import sys, pygame
from pygame import *


def main():
    pygame.init()

    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Juego del topo')

    # casa = image.load("hogar.png")
    # casa = transform.scale(casa, (100, 100))
    direccion_personaje_x = 20
    direccion_personaje_y = 90


    while True:

        ventana.fill((0, 0, 0))
        # ventana.blit(casa, (direccionx, direcciony, 50, 50))
        pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(direccion_personaje_x, direccion_personaje_y, 10, 10))

        n = 20
        for i in range(30):
            pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(n, 100, 10, 2))
            n = n + 12

        direccion_topo_x = 20
        direccion_topo_y = 90
        for i in range(4):
            pygame.draw.rect(ventana, (155, 155, 155), pygame.Rect(direccion_topo_x, direccion_topo_y, 10, 10))

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                tecla_presionada = key.name(event.key)

                if tecla_presionada == '1':
                    direccion_personaje_x += 12
                if tecla_presionada == '2':
                    direccion_personaje_x += 24

            if event.type == QUIT:
                sys.exit()

        display.flip()


main()
