import pygame

class Settings:

    def __init__(self):
        ''' Inicjalizacja ustawień gry. '''
        # Ustawienia ekranu
        self.screen = pygame.display.set_mode()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

        # Prędkość statku
        self.ship_speed = 3

        # Ustawienia dotyczące pocisku:
        self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Ustawienie dotyczące obcych
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # ustawienia gwiazd
        self.stars_speed = 3
        self.stars_frequency = 5
