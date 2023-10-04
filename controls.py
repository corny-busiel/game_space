import pygame
import sys
from bullet import Bullet
from ino import Ino
import time


right_mouse_button_pressed = False

def event(screen, gun, bullets, stat):
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
                elif event.key == pygame.K_ESCAPE:
                    stat.run_game = not stat.run_game
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

def update(bacground_color ,screen,stat,scores, gun,inos, bullets ):
    screen.fill(bacground_color)
    scores.show_score()
    for bullet in bullets:
        bullet.draw_bullet()
    gun.output() # функция отображение пушки
    inos.draw(screen)
    pygame.display.flip() 
    
def update_bullets(screen, stats, scores,inos , bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 1 * len(inos)
        scores.image_score()
    
def create_game_if(inos, bullets, screen, gun):
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(2)

def gun_kill(gun, stat, screen, inos, bullets):
    if stat.gun_left > 0:
        stat.gun_left -= 1
        create_game_if(inos, bullets, screen, gun)
        print(stat.gun_left)
    else:
        stat.run_game = False
        print("Проиграл")
        create_game_if(inos, bullets, screen, gun)
        stat.gun_left = 3
        stat.run_game = True
         
def update_inos(gun,stats, screen, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollide(gun, inos, True, None):
        gun_kill(gun,stats, screen, inos, bullets)
    inos_check(stats,screen,gun, inos,bullets)  

def create_army(screen, inos):
    ino = Ino(screen)
    number_ino_x = 22
    
    for row_ino in range(150):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = 50 + 50 * ino_number
            ino.y = -50 + -50 * row_ino
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)
            
def inos_check(stats, screen, gun, inos, bullets):
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(gun,stats, screen, inos, bullets)
            break