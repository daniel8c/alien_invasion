import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    ''' Klasa przedstawiająca pojedynczego obcego we flocie'''

    def __init__(self, ai_game):
        ''' Inicjalizacja obcego i zdefiniowanie jego położenia początkowego. '''

        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Wczytanie obrazu obcego i pobranie jego prostokąta
        self.image = pygame.image.load(r'images/alien.png')
        self.rect = self.image.get_rect()

        # Obcy pojawia się na górze po lewej stronie ekranu
        self.rect.topleft = self.screen_rect.topleft

        # Położenie poziome jest przechowywane w postaci liczby zmiennoprzcinkowej
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        ''' Przesunięcie ibcego w prawo lub w lewo. '''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x