import sys, pygame
from pygame import *


def main():
    pygame.init()

    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Juego del topo')

    # casa = image.load("hogar.png")
    # casa = transform.scale(casa, (100, 100))
    direccionx = 20
    direcciony = 90

    while True:

        ventana.fill((0, 0, 0))
        # ventana.blit(casa, (direccionx, direcciony, 50, 50))
        pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(direccionx, direcciony, 10, 10))

        n = 20
        for i in range(30):
            pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(n, 100, 10, 2))
            n = n + 12

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                tecla_presionada = key.name(event.key)

                if tecla_presionada == '1':
                    direccionx += 12
                if tecla_presionada == '2':
                    direccionx += 24

            if event.type == QUIT:
                sys.exit()

        display.flip()


main()
