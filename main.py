import pygame
from pygame.sprite import Group
import controls

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Космическая игра")
    bacground_color = (0,0,0)
    
    while True:
        controls.event()
        controls.update(bacground_color, screen)
    
    
def main():
    run() # главная функция игры запуска
    
if __name__ == "__main__":
    main()