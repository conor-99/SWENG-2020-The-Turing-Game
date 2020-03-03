# Class worked on by: Claire
import random
from personality import Personality

class Teenager(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(13, 21)
    
    def addPersonality(self, input):
        output = textSubstitution(input)
        return output

    # Add text substitution to the input.
    def textSubstitution(self, input):
        # Adding spelling mistakes should not happen everytime.
        if random.randint(1,5) == 1:
            addSpellingMistakes(input)
        
        # Shortening words continuously is far more common.
        shortenWords(input)
        return

    # Substitute words with common misspellings IF APPROPRIATE. - Luiz Fellipe
    def addSpellingMistakes(self, input):
        return

    # You -> u for instance, more likely to be commonly appropriate. - Kishore
    def shortenWords(self, input):
        return
