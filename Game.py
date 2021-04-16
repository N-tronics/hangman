"""
This game first displays the menu and then on the same window, displays the game.
"""

import pygame


class Game(object):
    def __init__(self, dimensions=(800, 500)):
        # Inits
        pygame.init()
        self.WIN_WIDTH, self.WIN_HEIGHT = dimensions
        self.WIN = pygame.display.set_mode(dimensions)
        pygame.display.set_caption('Hangman!')
        self.WAIT_TIME = 3000

        # Fonts
        self.LETTER_FONT = pygame.font.SysFont('comicsans', 40)
        self.WORD_FONT = pygame.font.SysFont('comicsans', 60)
        self.TITLE_FONT = pygame.font.SysFont('comicsans', 70)
        self.GAME_STATUS = pygame.font.SysFont('comicsans', 100)

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        # self.RED = (255, 0, 0)

        # Game variables
        self.FPS = 120
        self.clock = pygame.time.Clock()
        self.HALF_DISPLAY_X = self.WIN_WIDTH / 2
