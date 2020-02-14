# Class worked on by: Claire, Diego, Kishore
import re

class DataPreProcessor:
    # Creates an instance of the preprocessor with input being input from commandline passed to it from main class.
    def __init__(self, input):
        self.input = input
    
    # Processes the input.
    def processInput(self):
        self.convertAccentedCharsToAscii()
        self.lowerCase()
        self.convertNumberWordToDigit()
        self.removeNumbers()

    # Change accented characters eg. é to e. - Diego
    def convertAccentedCharsToAscii(self):

        self = re.sub(u"[àáâãäå]", 'a', self)
        self = re.sub(u"[èéêë]", 'e', self)
        self = re.sub(u"[ìíîï]", 'i', self)
        self = re.sub(u"[òóôõö]", 'o', self)
        self = re.sub(u"[ùúûü]", 'u', self)
        self = re.sub(u"[ýÿ]", 'y', self)


        return self

    # Put all text to lowercase.- Diego
    def lowerCase(self):
        self.lowerCase()
        return self

    # Convert one to 1. - Kishore
    def convertNumberWordToDigit(self):
        from word2number import w2n
        print w2n.word_to_num(self)
        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
     
        result = ''.join([i for i in self if not i.isdigit()])
        print(result)
        return result
