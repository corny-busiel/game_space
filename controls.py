import pygame
import sys

def event(gun):
    for event in pygame.event.get():
        # событие выхода
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    gun.mright = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    gun.mleft = True
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    gun.mup = True
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    gun.mdown = True
        # событие отпущенной клавиши
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    gun.mright = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    gun.mleft = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    gun.mup = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    gun.mdown = False

def update(bacground_color,screen,gun):
    screen.fill(bacground_color)
    gun.output() # функция отображение пушки
    pygame.display.flip() 