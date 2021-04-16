"""
Creates the Hangman UI.
"""

import pygame
import sys
import os
from math import sqrt
from RandomWord import RandomWord


class Hangman(object):
    def __init__(self, imgs, game, menu, difficulty='easy'):
        self.game = game
        self.menu = menu
        self.difficulty = difficulty

        self.load_images(imgs)

    def create_buttons(self, radius, guessed):
        GAP = 15
        letters = []
        start_x = round((self.game.WIN_WIDTH - (radius * 2 + GAP) * 13) / 2)
        start_y = 400
        alphabet = 65
        for i in range(26):
            if chr(alphabet + i) not in guessed:
                x = start_x + GAP * 2 + (radius * 2 + GAP) * (i % 13)
                y = start_y + ((i // 13) * (GAP + radius * 2))
                letters.append([x, y, chr(alphabet + i), True])

        return letters

    def draw(self, hangman_status, imgs, letters, radius, guessed, word, won):
        # Main screen
        self.game.WIN.fill(self.game.WHITE)
        title = self.game.TITLE_FONT.render('HANGMAN', True, self.game.BLACK)
        self.game.WIN.blit(title, (self.game.WIN_WIDTH / 2 - title.get_width() / 2, 20))
        self.game.WIN.blit(imgs[hangman_status], (150, 100))

        # Buttons
        for letter_coords in letters:
            x, y, lttr, visible = letter_coords
            if visible:
                pygame.draw.circle(self.game.WIN, self.game.BLACK, (x, y), radius, 3)
                text = self.game.LETTER_FONT.render(lttr, True, self.game.BLACK)
                self.game.WIN.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        # Word
        display_word = ''
        for letter in word:
            if letter in guessed:
                display_word += letter + ' '
            else:
                display_word += '_ '
        text = self.game.WORD_FONT.render(display_word, True, self.game.BLACK)
        self.game.WIN.blit(text, (400, 200))

        pygame.display.update()

        # Winning
        if won:
            # print('You Won!')
            pygame.time.delay(1000)
            game_status = 'YOU WON!'
            game_status_text = self.game.GAME_STATUS.render(game_status, True, self.game.BLACK)
            self.game.WIN.fill(self.game.WHITE)
            self.game.WIN.blit(game_status_text, (self.game.WIN_WIDTH / 2 - game_status_text.get_width() / 2,
                                                  self.game.WIN_HEIGHT / 2 - game_status_text.get_height() / 2))
            pygame.display.update()
            pygame.time.wait(self.game.WAIT_TIME)
            # self.main()
            self.menu.main()
        if hangman_status == 6:
            # print('You Lost!')
            pygame.time.delay(1000)
            game_status = 'YOU LOST!'
            game_status_text = self.game.GAME_STATUS.render(game_status, True, self.game.BLACK)
            self.game.WIN.fill(self.game.WHITE)
            self.game.WIN.blit(game_status_text, (self.game.WIN_WIDTH / 2 - game_status_text.get_width() / 2,
                                                  self.game.WIN_HEIGHT / 2 - game_status_text.get_height() / 2))

            actual_word = self.game.TITLE_FONT.render(word, True, self.game.BLACK)
            self.game.WIN.blit(actual_word, (self.game.WIN_WIDTH / 2 - actual_word.get_width() / 2,
                                             (self.game.WIN_HEIGHT / 2) + actual_word.get_height() + 50
                                             - actual_word.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(self.game.WAIT_TIME)
            # self.main()
            self.menu.main()

    def main(self):
        # Game Variables
        hangman_status = 0
        RADIUS = 20
        word_builder = RandomWord(self.difficulty)
        word, hint = word_builder.get_words()
        guessed = []
        for i in hint:
            guessed.append(i)
        letters = self.create_buttons(RADIUS, guessed)

        while True:
            self.game.clock.tick(self.game.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for letter in letters:
                        x, y, lttr, visible = letter
                        if visible:
                            dis = sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                            if dis < RADIUS:
                                letter[3] = False
                                if lttr in word:
                                    guessed.append(lttr)
                                else:
                                    hangman_status += 1

            won = True
            for lttr in word:
                if lttr not in guessed:
                    won = False
                    break

            self.draw(hangman_status, self.images, letters, RADIUS, guessed, word, won)

    
    def load_images(self, imgs):
        self.images = []
        for img_index in range(7):
            os.chdir(os.path.dirname(__file__))
            path = os.getcwd() + '/' + imgs + '/hangman' + str(img_index) + '.png'
            img = pygame.image.load(path)
            self.images.append(img)
