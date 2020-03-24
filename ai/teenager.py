# Class worked on by: Claire
import random
import string
from personality import Personality
from data_pre_processor import DataPreProcessor


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
        shortWords = {
	        'your' : 'ur',
            'tonight' : '2nite',
            'for you information' : 'fyi',
            'okay' : 'k',
            'ok':'k',
	        'to' : '2',
	        'tomorrow' : '2moro',
            'easy' : 'ez',
            'see you' : 'cya',
            'because' : 'cuz',
            'you' : 'u',
            }       
        
        input = self.string2Array(self.input)    
        input = self.string2Array(input)    
        for x in range(0,len(input)):
            for y in shortWords:
                if(str(input[x]) == y):
                    input[x] = shortWords[y]
        self.input = self.array2String(input)               
        return        input = self.array2String(input)               
        
        return input