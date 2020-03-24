# Class worked on by: Claire
import random
from personality import Personality

class YoungAdult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(22, 28)
        self.probSpellingMistake = random.randint(2,5)
    
    def addPersonality(self, input):
        output = self.shortenWords(input)
        return output

    # You -> u for instance, more likely to be commonly appropriate. Needs to return a string. - Kishore
    def shortenWords(self, input):
        return input

    # Add appropriate emjois - Luiz Fellipe
    def addEmojis(self, input):
        return input
    