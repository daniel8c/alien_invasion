import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """ Class intended for ship management. """

    def __init__(self, ai_game):
        """ Initialization of the spacecraft and its initial position. """

        super().__init__()

        self.screen = ai_game.settings.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Loads the spacecraft image and retrieves its rectangle.
        self.image = pygame.image.load(r'images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new spaceship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # The ship's horizontal position is stored as a floating point number.
        self.x = float(self.rect.x)

        # Options that indicate the movement of the ship.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Upgrade the ship's movement based on the option that indicates its movement. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Updating the rect object based on the self value.
        self.rect.x = self.x

    def blitme(self):
        """ Displaying a spaceship in its current position. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Center ship. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
