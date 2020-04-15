# coding=utf-8
# Class worked on by: Claire, Diego, Kishore, Leo
import re, os
from spellchecker import SpellChecker
from word2number import w2n
from string import digits

class DataPreProcessor:
    # Creates an instance of the preprocessor with pass input
    def __init__(self, input):
        self.input = input

    # Processes the input, applying our various changes to prepare it for the model
    def processInput(self, string):
        self.input = string
        self.convertAccentedCharsToAscii()
        self.removeNumbers()
        # word2number library sometimes changes our strings to ints, so we just double check that hasn't happened
        self.input = str(self.input)
        self.autoCorrect()
        self.removeNumWords()
        return self.checkLength()

    # Checks the input string to make sure we are working with more than three words
    # This is the minimum amount that will (almost) guarantee a response from the AI
    # This is only used for terminalMode(), as we can handle this on client-side more easily
    def checkLength(self):
        if len(self.string2Array(self.input)) < 3:
            return False
        else:
            return True

    # Rids the input of spelling mistakes, replacing with the most similar correctly spelled word
    def autoCorrect(self):
        if str(self.input).isspace():
            return
        spellchecker = SpellChecker()
        input = self.string2Array(self.input)
        spellchecker.unknown(input)
        output = []
        for x in range(len(input)):
            output.append(spellchecker.correction(input[x]))
        self.input = self.array2String(output)
        return

    # Convert a ' ' (space) delimited string to a list of words
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

    # Convert an array to a single string
    def array2String(self, array):
        string = ""
        for x in array:
            string += str(x) + " "
        string = string[0:-1]
        return string

    # Change accented characters eg. é to e
    # This is useful as we currently only support English
    def convertAccentedCharsToAscii(self):
        self.input = re.sub(r'[àáâãäåæÀÁÂÃÄÅÆ]', 'a', self.input)
        self.input = re.sub(r'[èéêëÈÉÊË]', 'e', self.input)
        self.input = re.sub(r'[ìíîïÌÍÎÏ]', 'i', self.input)
        self.input = re.sub(r'[òóôõöðøōŏőÒÓÔÕÖØŌŎŐ]', 'o', self.input)
        self.input = re.sub(r'[ùúûüũūŭůűųÙÚÛÜŨŪŬŮŰŲ]', 'u', self.input)
        self.input = re.sub(r'[ýÿŷÝŸ]', 'y', self.input)
        return

    # Convert words of numbers to actual numbers.
    def removeNumWords(self):
        numWords = [
        "zero", "Zero", "one", "One", "two","Two", "three", "Three", "four", "Four", "five", "Five", "six", "Six", "seven","Seven", "eight", "Eight",
        "nine", "Nine", "ten", "Ten", "eleven", "Eleven", "twelve", "Twelve", "thirteen", "Thirteen", "fourteen", "Fourteen", "fifteen", "Fifteen",
        "sixteen", "Sixteen", "seventeen", "Seventeen", "eighteen", "Eighteen", "nineteen", "Nineteen","twenty", "Twenty", "thirty", "Thirty", "forty", "Forty", 
        "fifty", "Fifty", "sixty", "Sixty", "seventy", "Seventy", "eighty", "Eighty", "ninety", "Ninety",
        "hundred", "Hundred", "thousand", "Thousand", "million", "Million", "billion", "Billion", "Trillion"]
        input = self.string2Array(self.input)
        errorCounter = 0
        for x in range(0,len(input)):
            for y in numWords:
                if(str(input[x]) == y):
                    try:                        
                        input[x] = ""
                    except:
                        errorCounter = errorCounter + 1               
        self.input = self.array2String(input)
        self.input = re.sub(' +', ' ', self.input)  
        return

    # Remove all numeric characters
    # The AI has trouble with numbers in general
    def removeNumbers(self): 
        input = self.string2Array(self.input)
        for x in range(0,len(input)):
           if((str(input[x]).isnumeric() == True)):
               input[x] = " "         
        self.input = self.array2String(input)
        self.input = re.sub(' +', ' ',self.input) 
        return