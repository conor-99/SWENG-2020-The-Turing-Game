# Class worked on by: Claire, Diego, Kishore, Leo
import re, os
from spellchecker import SpellChecker
from word2number import w2n
from string import digits

class DataPreProcessor:
    input = 0
    # Creates an instance of the preprocessor with input being input from commandline passed to it from main class.
    def __init__(self, input):
        self.input = input

    # Processes the input
    def processInput(self):
        self.convertAccentedCharsToAscii()
        self.removeNumbers()
        self.convertNumberWordToDigit()
        # This is only relevant because of the weird library
        self.input = str(self.input)
        self.autoCorrect()
        return

    # Rids the input of spelling mistakes, replacing with the most similar correctly spellled word
    def autoCorrect(self):
        spellchecker = SpellChecker()
        input = self.string2Array(self.input)
        spellchecker.unknown(input)
        output = []
        for x in range(len(input)):
            output.append(spellchecker.correction(input[x]))
        self.input = self.array2String(output)
        return

    # Convert a ' ' delimited string to a list of words
    # This will be deleted later, it is for testing purposes
    def string2Array(self, string):
        while(1 and len(string) > 0):
            if(string[0] == " "):
                string = string[1:len(string)]
            else:
                break
        array = []
        temp = ""
        for x in string:
            if(x != " "):
                temp += x
            else:
                array.append(temp)
                temp = ""
        array.append(temp)
        return array

    # Convert an array of words back to a string
    def array2String(self, array):
        string = ""
        for x in array:
            string += x + " "
        string = string[0:-1]
        return string

    # Change accented characters eg. é to e. - Diego
    def convertAccentedCharsToAscii(self):
        self.input = re.sub(r'[àáâãäåæÀÁÂÃÄÅÆ]', 'a', self.input)
        self.input = re.sub(r'[èéêëÈÉÊË]', 'e', self.input)
        self.input = re.sub(r'[ìíîïÌÍÎÏ]', 'i', self.input)
        self.input = re.sub(r'[òóôõöðøōŏőÒÓÔÕÖØŌŎŐ]', 'o', self.input)
        self.input = re.sub(r'[ùúûüũūŭůűųÙÚÛÜŨŪŬŮŰŲ]', 'u', self.input)
        self.input = re.sub(r'[ýÿŷÝŸ]', 'y', self.input)
        return

    # Convert one to 1. - Kishore
    def convertNumberWordToDigit(self):
        try:
            self.input = w2n.word_to_num(self.input)
            print('\033[93m' + "The original input has been overwritten by this function." + '\033[0m')
        except Exception as e:
            return
        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
        self.input = ''.join([i for i in self.input if not i.isdigit()])
        self.input = (self.input).replace("_", " ")
        return
