# Class worked on by: Claire
import random
import string

from personality import Personality


class Teenager(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(13, 21)
        self.probSpellingMistake = random.randint(1,5)

    def addPersonality(self, input):
        output = self.shortenWords(input)
        return output

    # You -> u for instance, more likely to be commonly appropriate. Needs to return a string. - Kishore
    def shortenWords(self, input):
        return