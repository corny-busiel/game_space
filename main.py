import pygame
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Космическая игра")
    bacground_color = (0,0,0)
    
    while True:
       screen.fill(bacground_color)      
       pygame.display.flip()      
    
    
def main():
    run() # главная функция игры запуска
    
if __name__ == "__main__":
    main()