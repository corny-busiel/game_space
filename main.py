import pygame
from pygame.sprite import Group
import controls
from gun import Gun
import stats
import time


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Космическая игра")
    gun = Gun(screen)
    bacground_color = (0,0,0)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stat = stats.Stats()
    
    
    while True:
        controls.event(screen, gun, bullets)
        controls.update(bacground_color ,screen, gun,inos, bullets )
        controls.update_bullets(inos , bullets)
        controls.update_inos(gun,stat, screen, inos, bullets)
        gun.update_gun()# вызов функции обновление позиции пушки

        
def main():
    run() # главная функция игры запускаd
    
if __name__ == "__main__":
    main()