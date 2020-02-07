# Class worked on by: Claire, Diego

class DataPreProcessor:
    # Creates an instance of the preprocessor with input being input from commandline passed to it from main class.
    def __init__(self, input):
        self.input = input
    
    # Processes the input to all lower case and punctuation removed.
    def processInput(self):
        return processedInput