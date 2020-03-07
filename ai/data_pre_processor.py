# coding=utf-8
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
        self.convertNumberWordToDigit()
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
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]
        
        input = self.string2Array(self.input)
        errorCounter = 0

        for x in range(0,len(input)):
            for y in units:
                if(input[x] == y):
                    try:
                        test = str(w2n.word_to_num(input[x+1]))                   
                        for a in scales:
                            if((str(input[x+1])) == a):                                           
                                            try:
                                                    test = w2n.word_to_num(input[x+2])
                                                    input [x+2] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1])* w2n.word_to_num(input[x+2]))
                                                    input[x]= ""
                                                    input[x + 1]= ""
                                            except:                                    
                                                    input[x + 1] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1]))
                                                    input[x]= ""                                                    
                    except:                       
                        input[x] = str(w2n.word_to_num(input[x]))
            for z in tens:            
                if(input[x] == z):                   
                    try:
                        test = w2n.word_to_num(input[x+1])
                        for b in units:
                            if(str(input[x+1]) == b):                                            
                                    input [x+1] = str(w2n.word_to_num(input[x]) + w2n.word_to_num(input[x+1]))
                                    input[x]= ""                                                                  
                                    for c in scales:                                        
                                        try:
                                            if((str(input[x+2])) == c):                                            
                                                try:
                                                        test = w2n.word_to_num(input[x+3])
                                                        input [x + 3] = str(w2n.word_to_num(input[x + 1]) * w2n.word_to_num(input[x+2])* w2n.word_to_num(input[x+3]))
                                                        input[x + 1]= ""
                                                        input[x + 2]= ""
                                                except:                                    
                                                        input[x + 2] = str(w2n.word_to_num(input[x + 1]) * w2n.word_to_num(input[x+2]))
                                                        input[x + 1]= ""  
                                        except: 
                                                errorCounter = errorCounter + 1

                        for d in scales: 
                            if((str(input[x+1])) == d):                                            
                                            try:
                                                    test = w2n.word_to_num(input[x+2])
                                                    input [x + 2] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1])* w2n.word_to_num(input[x+2]))
                                                    input[x]= ""
                                                    input[x + 1]= ""
                                            except:
                                    
                                                    input[x + 1] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1]))
                                                    input[x]= ""                                                                                                                       
                    except:
                                                    input [x] = str(w2n.word_to_num(input[x]))            
        andIndex = 0
        beforeAndIndex =0
        afterAndIndex = 0
        valueBeforeAndIndex = 0
        valueAfterAndIndex = 0
        finalValue = 0

        for x in range(len(input)):                             
            try:
                if((str(input[x]) == "a") and (str(input[x + 1]) == "a")):
                        input[x] = ""
                        input[x+1] = ""
                if((str(input[x]) == "a") and (str(input[x + 1]).isnumeric() == True)):
                        input[x] = ""
            except:
                errorCounter = errorCounter + 1
            if(str(input[x]) == "and"):
                andIndex=x
                beforeAndIndex = x - 1
                afterAndIndex = x + 1                                
                if(input[beforeAndIndex].isnumeric() == True):
                        valueBeforeAndIndex = int(str(input[beforeAndIndex]))                
                        if(valueBeforeAndIndex > 99):
                            input[andIndex] = ""
                            try:
                                if(input[afterAndIndex].isnumeric() == True):                                
                                    valueAfterAndIndex = int(str(input[afterAndIndex]))
                                    finalValue = valueBeforeAndIndex  + valueAfterAndIndex
                                    input[beforeAndIndex] = ""
                                    input[afterAndIndex] = str(finalValue)
                            except:
                                    errorCounter = errorCounter + 1                                  
                            try:
                                    if(input[afterAndIndex + 1].isnumeric() == True):                              
                                
                                        valueAfterAndIndex = int(str(input[afterAndIndex + 1]))
                                        finalValue = valueBeforeAndIndex  + valueAfterAndIndex
                                        input[beforeAndIndex] = ""
                                        input[afterAndIndex + 1] = str(finalValue)
                            except:
                                    errorCounter = errorCounter + 1
        print(input)
        self.input = self.array2String(input)
        print(self.input)
                  
        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):   
        input = self.string2Array(self.input)
        for x in range(0,len(input)):
           if((str(input[x]).isnumeric() == True)):
               input[x] = " "         
        self.input = self.array2String(input) 
        #input = ''.join([i for i in input if not i.isdigit()])
        return


