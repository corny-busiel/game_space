import pygame
from pygame.sprite import Group
import controls
from gun import Gun
import stats
import time
from scores import Scores


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
    scores = Scores(screen, stat)
    
    
    while True:
        controls.event(screen, gun, bullets, stat)
        if stat.run_game:
            controls.update(bacground_color ,screen,stat,scores, gun,inos, bullets )
            controls.update_bullets(screen, stat, scores,inos , bullets)
            controls.update_inos(gun,stat, screen, inos, bullets)
            gun.update_gun()# вызов функции обновление позиции пушки

        
def main():
    run() # главная функция игры запускаd
    
if __name__ == "__main__":
    main()