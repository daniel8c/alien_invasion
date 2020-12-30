import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class representing the single alien in the fleet. """

    def __init__(self, ai_game):
        """ Alien initialization and definition of its initial position. """

        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load alien image and its rectangle.
        self.image = pygame.image.load(r'images/alien.png')
        self.rect = self.image.get_rect()

        # The alien appears at the top left of the screen.
        self.rect.topleft = self.screen_rect.topleft

        # The horizontal position is stored as a float number.
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """ Move the alien right or left. """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
