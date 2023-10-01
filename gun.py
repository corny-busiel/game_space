import pygame

class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("image/gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx # позиция пушки в центре
        
        self.rect.bottom = self.screen_rect.bottom # позиция пушки снизу
        self.mright = False # переменная передвижение права
        self.mleft = False # лево
        self.mup = False # вверх
        self.mdown = False # вниз
        
    def output(self): # функция отображение пушки
        self.screen.blit(self.image, self.rect)
        
    def update_gun(self): # функция обновления позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1.8
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1.8
        if self.mup and self.rect.top > 500:
            self.rect.centery -= 1.8
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1.8