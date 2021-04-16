"""
Creates a random hint according to a given difficulty.
"""

from random import choice, randint
from os import path


class RandomWord(object):
    def __init__(self, diff):
        self.diff = diff

        self.get_random_word()
        self.create_hint()

    def get_random_word(self):
        words = []
        f = open(path.join('words.txt'))
        for word in f:
            if 6 > len(word[0:-1]) > 3:
                words.append(word[0:-1].upper())

        self.word = choice(words)

    def create_hint(self):
        word_len = len(self.word)
        self.hint = []
        indexes = []
        if self.diff == 'easy':
            self.hint_counter = round(0.6 * word_len)
        elif self.diff == 'medium':
            self.hint_counter = round(0.35 * word_len)
        else:
            self.hint_counter = round(0.2 * word_len)

        for _ in range(self.hint_counter):
            lttr_index = randint(0, word_len - 1)
            if lttr_index not in indexes:
                self.hint.append(self.word[lttr_index])
                indexes.append(lttr_index)

    def get_words(self):
        return self.word, self.hint
