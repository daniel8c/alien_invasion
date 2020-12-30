import pygame


class Settings:

    def __init__(self):
        """ Initializing game settings. """

        # Screen settings
        self.screen = pygame.display.set_mode()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Aliens settings
        self.fleet_drop_speed = 30

        # Stars settings
        self.stars_frequency = 10

        # Easy a game speed change
        self.speedup_scale = 1.2

        # Easy scoring change
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change during the game. """
        self.ship_speed = 1.8
        self.bullet_speed = 3
        self.alien_speed = 1.1
        self.stars_speed = 1.5

        # Scoring
        self.alien_points = 50

        # Value fleet_direction 1 right, -1 left.
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.stars_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
