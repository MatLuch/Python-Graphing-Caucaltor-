import pygame 
from colors import * 
pygame.init()

def draw(screen, x, y):
    pygame.draw.circle(screen, blue, (x, y), 5)

def graph(screen, points):

        screen.fill(white)

        pygame.draw.line(screen, black, (500, 1000), (500, 0), 2)

        pygame.draw.line(screen, black, (0, 500), (1000, 500), 2)

        for point in points:
              draw(screen, point[0], point[1])
        pygame.display.update()

