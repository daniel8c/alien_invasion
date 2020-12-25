class Settings:

    def __init__(self):
        ''' Inicjalizacja ustawień gry. '''
        # Ustawienia ekranu
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed = 2

        # Ustawienia dotyczące pocisku:
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

