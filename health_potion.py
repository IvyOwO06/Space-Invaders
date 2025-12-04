import pygame

class Health_potion(pygame.sprite.Sprite):
    def __init__(self, x, screen_height):
        super().__init__()
        self.x = x
        self.screen_height = screen_height
        self.image = pygame.image.load("Graphics/health_potion.png")
        self.rect = self.image.get_rect(bottomleft = (self.x, self.screen_height))