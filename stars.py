import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    ''' Klasa przedstawiająca gwiazdę'''

    def __init__(self, ai_game):
        ''' Inicjalizacja gwizdy i zdefiniowanie jej położenia początkowego. '''

        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Wczytanie obrazu gwiazdy i pobranie jej prostokąta
        self.image = pygame.image.load(r'images/star_2.svg')
        self.rect = self.image.get_rect()

        # gwiazda pojawi się na górze ekranu w wylosowanym miejscu
        self.screen_rect.x = random.randint(0, self.screen_rect.width)
        self.screen_rect.y = 0

        # Położenie poziome jest przechowywane w postaci liczby zmiennoprzcinkowej
        self.x = float(self.screen_rect.x)
        self.y = float(self.screen_rect.y)

    def update(self):
        '''Poruszanie się gwiazdy po ekranie'''

        # Uaktualnienie położenia pocisku
        self.y += self.settings.stars_speed

        # Uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y
        self.rect.x = self.x
