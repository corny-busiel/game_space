import pygame
import sys
from bullet import Bullet

def event(screen, gun, bullets):
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
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

def update(bacground_color,screen,gun, bullets, ino):
    screen.fill(bacground_color)
    for bullet in bullets:
        bullet.draw_bullet()
    gun.output() # функция отображение пушки
    ino.draw_ino()
    pygame.display.flip() 
    
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)