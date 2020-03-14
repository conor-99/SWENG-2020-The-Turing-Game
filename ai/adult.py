# Class worked on by: Claire
import random
from personality import Personality

class Adult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(29, 40)
        self.probSpellingMistake = random.randint(5,7)
    
    def addPersonality(self, input):
        output = self.addPunctuation(input)
        return output

    # The returned string from the AI model does not have any punctuation. 
    # This function needs to add punction to that string and return it. - Diego
    def addPunctuation(self, input):
       # input = "hello how are you i cant hear you and i cant see"
        input = input + '.'
        input = input.replace('cant', 'can^t')
        input = input.replace('hello', 'hello!')
        input = input.replace('isnt', 'isn^t')
        input = input.replace('would', 'wouldn^t')
        input = input.replace('hadnt', 'hadn^t')
        input = input.replace('how are you', 'how are you?')
        input = input.replace('where are you', 'where are you?')
        input = input.replace('are you going?', 'how are you?')
        input = input.replace('however', 'however,')
       # print(input)

	