import pygame.font

class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 46)
        self.image_score()
        
    def image_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (50,50,50))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = self.screen_rect.top + 30
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)