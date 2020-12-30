import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    """ A class representing a star."""

    def __init__(self, ai_game):
        """ Star initialization and definition of its initial position. """

        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Loads the star image and retrieves its rectangle
        self.image = pygame.image.load(r'images/star_2.svg')
        self.rect = self.image.get_rect()

        # A star will appear at the top of the screen in the randomized location
        self.screen_rect.x = random.randint(0, self.screen_rect.width)
        self.screen_rect.y = 0

        # The horizontal and vertical position is stored as a floating point number
        self.x = float(self.screen_rect.x)
        self.y = float(self.screen_rect.y)

    def update(self):
        """ Movement of the star on the screen. """

        # Update bullet position
        self.y += self.settings.stars_speed

        # Updating the position of the bullet rectangle
        self.rect.y = self.y
        self.rect.x = self.x
