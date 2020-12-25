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

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load(r'images/alien.bmp')
        self.rect = self.image.get_rect()

        # Obcy pojawia się na górze po lewej stronie ekranu
        self.rect.topleft = self.screen_rect.topleft

        # Położenie poziome jest przechowywane w postaci liczby zmiennoprzcinkowej
        self.x = float(self.rect.x)



