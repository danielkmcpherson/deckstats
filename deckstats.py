

class DeckStats:
    """Overall class to manage program behaviour"""

    def __init__(self):
        """Initialize the program"""
        self.deck = Deck()
        


if __name__ == '__main__':
    # Make a game instance and run the game.
    ds = DeckStats()
    ds.run()