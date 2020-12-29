class GameStats:
    ''' Monitorowanie danych statystycznych w grze inwazja obcych. '''

    def __init__(self, ai_game):
        ''' Inicjalizacja danych statystycznych. '''
        self.settings = ai_game.settings
        self.reset_stats()
        # Uruchomienie gry 'Alien Invasion' w stanie aktywnym
        self.game_active = False

    def reset_stats(self):
        ''' Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry. '''

        self.ships_left = self.settings.ship_limit