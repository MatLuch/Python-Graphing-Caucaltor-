import pygame
from input import GetPoints
from colors import * 
from graph import graph
from graph import draw 
width = 1000
height = 1000

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graphing")

print("welcome to a simple graphing caucaltor")

print("what is the max number you will have in your graph: ")
max = int(input(""))
factor = max / 10
running = True

points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
    print("enter x then y")
    x, y = GetPoints()
    xPix = 500 + x * factor
    yPix = 500 - y * factor

    points.append((xPix, yPix))
    graph(screen, points)

pygame.quit()