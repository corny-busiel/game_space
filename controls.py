import pygame
import sys

def event():
    for event in pygame.event.get():
        # событие выхода
            if event.type == pygame.QUIT:
                sys.exit()

def update(bacground_color,screen):
    screen.fill(bacground_color)
    pygame.display.flip() 