import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):

    def __init__(self, screen):

        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the star image and get its rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Randomly position the star"""
        self.rect.centerx = randint(self.screen_rect.left, self.screen_rect.right)
        self.rect.centery = randint(self.screen_rect.top, self.screen_rect.bottom)
