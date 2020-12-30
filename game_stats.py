class GameStats:
    """ Monitoring the statistics of the game alien invasion. """

    def __init__(self, ai_game):
        """ Initializing data stats """
        self.settings = ai_game.settings
        self.reset_stats()
        # Launching the game 'Alien Invasion' in active state
        self.game_active = False

        # The best score
        self.high_score = 0

    def reset_stats(self):
        """ Initialization of statistical data that may change during the game. """

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0
