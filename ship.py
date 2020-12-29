import pygame


class Ship:
    ''' Klasa przeznaczona do zarządzania statkiem '''

    def __init__(self, ai_game):
        ''' Inicjalizacja statku kosmicznego i jego położenia początkowego. '''

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load(r'images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' Uaktualnienie poruszania się statku na podstawie opcji wskazującej na jego ruch. '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect na podstawie wartości self
        self.rect.x = self.x

    def blitme(self):
        ''' Wyświetlanie statku kosmicznego w jego aktualnym położeniu. '''
        self.screen.blit(self.image, self.rect)
