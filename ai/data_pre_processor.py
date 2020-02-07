# Class worked on by: Claire, Diego, Kishore

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
        return

    # Put all text to lowercase.- Diego
    def lowerCase(self):
        return

    # Convert one to 1. - Kishore
    def convertNumberWordToDigit(self):
        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
        return
