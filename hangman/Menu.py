"""
Creates the Menu UI.
"""

import pygame
import os
import sys
from Game import Game
from Hangman import Hangman


class Menu(object):
    def __init__(self, imgs):
        self.game = Game()
        self.imgs = imgs
        self.button_width = 200
        self.play_button_width = 400
        self.button_height = 50
        self.button_starting_height = 100
        self.diff = 'easy'
        self.easy_text_color = self.medium_text_color = self.hard_text_color = self.play_text_color = self.game.BLACK
        self.easy_bg_color = self.medium_bg_color = self.hard_bg_color = self.play_bg_color = self.game.WHITE

        # Game Constants
        self.DIFF_BUTTON_X_RANGE = (self.game.HALF_DISPLAY_X - self.button_width / 2,
                                    self.game.HALF_DISPLAY_X + self.button_width / 2)
        self.EASY_Y_RANGE = (self.button_starting_height,
                             self.button_starting_height + self.button_height)
        self.MEDIUM_Y_RANGE = (self.button_starting_height + 83,
                               self.button_starting_height + 83 + self.button_height)
        self.HARD_Y_RANGE = (self.button_starting_height + 83 * 2,
                             self.button_starting_height + 83 * 2 + self.button_height)

        self.PLAY_X_RANGE = (self.game.HALF_DISPLAY_X - self.play_button_width / 2,
                             self.game.HALF_DISPLAY_X + self.play_button_width / 2)
        self.PLAY_Y_RANGE = (self.button_starting_height + 83 * 4,
                             self.button_starting_height + 83 * 4 + self.button_height)

    def draw(self, easy, medium, hard, play):
        # White bg and title
        self.game.WIN.fill(self.game.WHITE)
        menu_title = self.game.TITLE_FONT.render('HANGMAN!', True, self.game.BLACK)
        self.game.WIN.blit(menu_title, (self.game.HALF_DISPLAY_X - menu_title.get_width() / 2, 20))

        # Buttons
        pygame.draw.rect(self.game.WIN, self.easy_bg_color, easy)
        pygame.draw.rect(self.game.WIN, self.medium_bg_color, medium)
        pygame.draw.rect(self.game.WIN, self.hard_bg_color, hard)
        pygame.draw.rect(self.game.WIN, self.play_bg_color, play)

        pygame.draw.rect(self.game.WIN, self.game.BLACK,
                         pygame.Rect((easy.x - 3, easy.y - 3), (easy.width + 6, easy.height + 6)), 2)
        pygame.draw.rect(self.game.WIN, self.game.BLACK,
                         pygame.Rect((medium.x - 3, medium.y - 3), (medium.width + 6, medium.height + 6)), 2)
        pygame.draw.rect(self.game.WIN, self.game.BLACK,
                         pygame.Rect((hard.x - 3, hard.y - 3), (hard.width + 6, hard.height + 6)), 2)
        pygame.draw.rect(self.game.WIN, self.game.BLACK,
                         pygame.Rect((play.x - 3, play.y - 3), (play.width + 6, play.height + 6)), 2)

        # Button text
        easy_text = self.game.LETTER_FONT.render('Easy', True, self.easy_text_color)
        self.game.WIN.blit(easy_text, (self.game.HALF_DISPLAY_X - easy_text.get_width() / 2,
                                       easy.y + easy_text.get_height() / 2))
        medium_text = self.game.LETTER_FONT.render('Medium', True, self.medium_text_color)
        self.game.WIN.blit(medium_text, (self.game.HALF_DISPLAY_X - medium_text.get_width() / 2,
                                         medium.y + medium_text.get_height() / 2))
        hard_text = self.game.LETTER_FONT.render('Hard', True, self.hard_text_color)
        self.game.WIN.blit(hard_text, (self.game.HALF_DISPLAY_X - hard_text.get_width() / 2,
                                       hard.y + hard_text.get_height() / 2))

        play_text = self.game.LETTER_FONT.render('Play', True, self.play_text_color)
        self.game.WIN.blit(play_text, (self.game.HALF_DISPLAY_X - play_text.get_width() / 2,
                                       play.y + play_text.get_height() / 2))

        pygame.display.update()

    def handle_button_presses(self):
        m_x, m_y = pygame.mouse.get_pos()
        if self.DIFF_BUTTON_X_RANGE[0] <= m_x <= self.DIFF_BUTTON_X_RANGE[1] and \
                self.EASY_Y_RANGE[0] <= m_y <= self.EASY_Y_RANGE[1]:
            self.diff = 'easy'
            self.easy_text_color = self.game.WHITE
            self.easy_bg_color = self.game.BLACK
        else:
            self.easy_text_color = self.game.BLACK
            self.easy_bg_color = self.game.WHITE

        if self.DIFF_BUTTON_X_RANGE[0] <= m_x <= self.DIFF_BUTTON_X_RANGE[1] and \
                self.MEDIUM_Y_RANGE[0] <= m_y <= self.MEDIUM_Y_RANGE[1]:
            self.diff = 'easy'
            self.medium_text_color = self.game.WHITE
            self.medium_bg_color = self.game.BLACK
        else:
            self.medium_text_color = self.game.BLACK
            self.medium_bg_color = self.game.WHITE

        if self.DIFF_BUTTON_X_RANGE[0] <= m_x <= self.DIFF_BUTTON_X_RANGE[1] and \
                self.HARD_Y_RANGE[0] <= m_y <= self.HARD_Y_RANGE[1]:
            self.diff = 'hard'
            self.hard_text_color = self.game.WHITE
            self.hard_bg_color = self.game.BLACK
        else:
            self.hard_text_color = self.game.BLACK
            self.hard_bg_color = self.game.WHITE

        if self.PLAY_X_RANGE[0] <= m_x <= self.PLAY_X_RANGE[1] and \
                self.PLAY_Y_RANGE[0] <= m_y <= self.PLAY_Y_RANGE[1]:
            self.launch_hangman(self.diff)
            self.play_text_color = self.game.WHITE
            self.play_bg_color = self.game.BLACK
        else:
            self.play_text_color = self.game.BLACK
            self.play_bg_color = self.game.WHITE

    def main(self):
        # Necessary changes
        self.easy_text_color = self.game.WHITE
        self.easy_bg_color = self.game.BLACK
        easy = pygame.Rect((self.game.HALF_DISPLAY_X - (self.button_width / 2), self.button_starting_height),
                           (self.button_width, self.button_height))
        medium = pygame.Rect((self.game.HALF_DISPLAY_X - (self.button_width / 2), self.button_starting_height + 83 * 1),
                             (self.button_width, self.button_height))
        hard = pygame.Rect((self.game.HALF_DISPLAY_X - (self.button_width / 2), self.button_starting_height + 83 * 2),
                           (self.button_width, self.button_height))
        play = pygame.Rect(
            (self.game.HALF_DISPLAY_X - (self.play_button_width / 2), self.button_starting_height + 83 * 4),
            (self.play_button_width, self.button_height))

        while True:
            self.game.clock.tick(self.game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_presses()

            self.draw(easy, medium, hard, play)

    def launch_hangman(self, diff):
        hangman = Hangman(self.imgs, self.game, self, diff)
        hangman.main()

