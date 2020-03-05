# Class worked on by: Claire
import random
from personality import Personality

class YoungAdult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(22, 28)
    
    def addPersonality(self, input):
        output = textSubstitution(input)
        return output

    # Add text substitution to the input.
    def textSubstitution(self, input):
        # Shortening words continuously is far more common.
        output = shortenWords(input)

        # Adding spelling mistakes should not happen everytime.
        if random.randint(1,5) == 1:
            output = addSpellingMistakes(input)
        return output

    # You -> u for instance, more likely to be commonly appropriate.Needs to return a string. - Kishore
    def shortenWords(self, input):
        return 

    # Substitute words with common misspellings IF APPROPRIATE. Needs to return a string. - Luiz Fellipe
    def addSpellingMistakes(self, input):
        return 