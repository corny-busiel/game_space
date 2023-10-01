import pygame
from pygame.sprite import Group
import controls
from gun import Gun


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Космическая игра")
    gun = Gun(screen)
    bacground_color = (0,0,0)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    
    while True:
        controls.event(screen, gun, bullets)
        controls.update(bacground_color ,screen, gun,inos, bullets )
        controls.update_bullets(bullets)
        gun.update_gun() # вызов функции обновление позиции пушки
    
    
def main():
    run() # главная функция игры запуска
    
if __name__ == "__main__":
    main()