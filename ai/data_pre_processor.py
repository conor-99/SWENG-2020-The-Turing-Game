# Class worked on by: Claire, Diego, Kishore
import re

class DataPreProcessor:
    input = 0
    # Creates an instance of the preprocessor with input being input from commandline passed to it from main class.
    def __init__(self, input):
        self.input = input

    # Processes the input.
    def processInput(self):
        self.convertAccentedCharsToAscii()
        self.input = self.input.lower()
        self.convertNumberWordToDigit()
        self.removeNumbers()
        return

    # Change accented characters eg. é to e. - Diego
    def convertAccentedCharsToAscii(self):
        self.input = re.sub(r'[àáâãäåæÀÁÂÃÄÅÆ]', 'a', self.input)
        self.input = re.sub(r'[èéêëÈÉÊË]', 'e', self.input)
        self.input = re.sub(r'[ìíîïÌÍÎÏ]', 'i', self.input)
        self.input = re.sub(r'[òóôõöðøōŏőÒÓÔÕÖØŌŎŐ]', 'o', self.input)
        self.input = re.sub(r'[ùúûüũūŭůűųÙÚÛÜŨŪŬŮŰŲ]', 'u', self.input)
        self.input = re.sub(r'[ýÿŷÝŸ]', 'y', self.input)
        self.input = re.sub(r'\W+', '_', self.input)
        return

    # Convert one to 1. - Kishore
    def convertNumberWordToDigit(self):
        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
        return
