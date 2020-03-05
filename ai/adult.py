# Class worked on by: Claire
import random
from personality import Personality

class Adult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(29, 40)
    
    def addPersonality(self, input):
        output = addPunctuation(input)
        return output

    # The returned string from the AI model does not have any punctuation. 
    # This function needs to add punction to that string and return. - Diego
    def addPunctuation(self, input):
        return 