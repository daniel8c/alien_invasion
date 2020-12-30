import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Class designed to manage bullets launched by a ship """

    def __init__(self, ai_game):
        """ Create bullet at the ship's current position. """

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rectangle at (0,0) and then define the appropriate location for it.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Position is defined by a float value.
        self.y = float(self.rect.y)

    def update(self):
        """ Moving bullet on the screen. """

        # Update bullet position.
        self.y -= self.settings.bullet_speed

        # Update bullet rectangle position.
        self.rect.y = self.y

    def draw_bullet(self):
        """ Display rectangle on the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
