import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from stars import Star


class AlienInvasion:
    ''' Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry. '''

    def __init__(self):
        ''' Inicjalizacja gry i utworzenie jej zasobów. '''
        # Zmienna kontrolująca iteracje
        self.i = 0

        # Inicjalizacja
        pygame.init()
        self.settings = Settings()

        # Zmienne ekranu
        self.screen = self.settings.screen

        # Egzemplarz statku
        self.ship = Ship(self)

        # Grupy
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        # Utworzenie floty
        self._create_fleet()

    def run_game(self):
        ''' Rozpoczęcie pętli głównej gry. '''
        while True:
            self.i += 1
            # Sprawdzanie zdarzeń
            self._check_events()
            # Uaktualnienie pozycji statku
            self.ship.update()
            # Uaktualnienie pozycji pocisku
            self._update_bullets()
            # Uaktualnienie pozycji obcych
            self._update_aliens()
            # Uaktualnienie pozycji gwiazd
            self._update_stars()
            # Uaktualnienie obrazów na ekranie
            self._update_screen()

    def _check_events(self):
        ''' Reakcja na zdarzenia generowane przez klawiaturę i mysz. '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        ''' Utworzenie nowego pocisku i dodanie go do grupy pocisków. '''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Uaktualnienie położenia pocisków i usunięcie tych niewidocznych'''
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        '''Utworzenie pełnej floty obcych'''

        # Ustalenie liczby obcych, którzy mieszczą się w rzędzie.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaliable_space_x // (2 * alien_width)

        # Ustalenie liczby rzędów
        ship_height = self.ship.rect.height
        avaliable_space_y = (self.settings.screen_height - (3 * alien_height)) - ship_height
        number_rows = avaliable_space_y // (2 * alien_height)

        # Utworzenie pełnej floty
        for number_row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, number_row)

    def _create_alien(self, alien_number, number_rows):
        '''Utworzenie obcego i umieszczenie go w rzędzie'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * number_rows
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _update_aliens(self):
        ''' Sprawdzanie czy flota obcych znajduje się przy krawędzi,
        a następnie uaktualnienie położenia wszystkich obcych we flocie. '''
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        ''' Odpowiednia reakcja gdy obcy dotrze do krawędzi ekranu '''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        ''' Przesunięcie całej floty w dół i zmiana kierunku w którym się ona porusza '''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _new_star(self):
        ''' Utworzenie gwiazdy '''
        if self.i % self.settings.stars_frequency == 0:
            new_star = Star(self)
            self.stars.add(new_star)

    def _update_stars(self):
        self._new_star()
        self.stars.update()

        for star in self.stars.copy():
            if star.rect.top >= self.settings.screen_height:
                self.stars.remove(star)

    def _update_screen(self):
        ''' Uaktualnienie obrazów na ekranie i przejście do nowego ekranu. '''

        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Wyświetlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()
