import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.initial_y = self.rect.centery

        self.center_ship()

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def center_ship(self):
        """Center the ship on the screen."""
        # Store a decimal value for the ship's center.
        self.real_centerx = float(self.screen_rect.centerx)
        self.real_centery = float(self.initial_y)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.real_centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.real_centerx -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.real_centery -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.real_centery += self.ai_settings.ship_speed_factor

        #Update rect object from self.real_center
        self.rect.centerx = int(self.real_centerx)
        self.rect.centery = int(self.real_centery)
