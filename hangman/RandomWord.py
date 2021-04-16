"""
Creates a random hint according to a given difficulty.
"""

from random import choice, randint
from os import path


class RandomWord(object):
    def __init__(self, diff):
        self.diff = diff

        self.get_random_word()
        # self.create_hint()
        self.classify_lttrs()

    def get_random_word(self):
        words = []
        f = open(path.join('words.txt'))
        for word in f:
            if len(word[0:-1]) > 3:
                words.append(word[0:-1].upper())

        self.word = choice(words)

    """def create_hint(self):
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
                indexes.append(lttr_index)"""

    def classify_lttrs(self):
        VOWELS = ['A', 'E', 'I', 'O', 'U']
        word_vowels = []
        word_consonants = []
        for lttr in self.word:
            if lttr in VOWELS:
                if lttr not in word_vowels:
                    word_vowels.append(lttr)
            else:
                if lttr not in word_consonants:
                    word_consonants.append(lttr)
        
        self.hint = self.generate_hint(word_vowels, word_consonants)
        while len(self.hint) < round(len(self.word) * 0.2):
            self.classify_lttrs()

    def generate_hint(self, vowels, consonants):
        hint = []

        # Easy difficulty
        if self.diff == 'easy':
            # Vowels
            i = 0
            if len(vowels) > 1: i = randint(1, 2)
            vowels = self.loop_and_remove(vowels, i)

            # Consonants
            j = randint(1, 2)
            consonants = self.loop_and_remove(consonants, j)
        
            for v in vowels:
                hint.append(v)
            for c in consonants:
                hint.append(c)

        # Medium difficulty
        if self.diff == 'medium':
            # Vowels
            i = 0
            if len(vowels) > 1: i = randint(1, 2) 
            vowels = self.loop_and_remove(vowels, i)

            # Consonants
            if len(consonants) > 3: j = randint(1, round(len(vowels) / 2))
            else: j = randint(1, 2)

            consonants = self.loop_and_remove(consonants, j)
        
            for v in vowels:
                hint.append(v)
            for c in consonants:
                hint.append(c)

        # Hard difficulty
        if self.diff == 'hard':
            # Vowels
            i = 0
            if len(vowels) > 1: i = randint(1, 2)
            vowels = self.loop_and_remove(vowels, i)

            # Consonants
            j = randint(1, len(consonants))
            consonants = self.loop_and_remove(consonants, j)
        
            for v in vowels:
                hint.append(v)
            for c in consonants:
                hint.append(c)


        return hint

    def loop_and_remove(self, alph, loop_limit):
        for _ in range(loop_limit):
            alph.remove(choice(alph))

        return alph

    def get_words(self):
        return self.word, self.hint
