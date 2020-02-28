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
        self.removeNumberWords
        # This is only relevant because of the weird library
        self.input = str(self.input)
        self.autoCorrect()
        self.removeNumberWords()
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
    def removeNumberWords(self):
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]
        
        input = self.string2Array(self.input)
        
        for x in range(len(input)):
            
            for y in units:
                
                if(input[x] == y):

                    try:

                        res = str(w2n.word_to_num(input[x+1]))
                    

                        for a in scales:
 
                            if((str(input[x+1])) == a):
                                            
                                            try:
                                                    result = w2n.word_to_num(input[x+2])
                                                    input [x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1])* w2n.word_to_num(input[x+2]))
                                                    input[x + 1]= ""
                                                    input[x + 2]= ""
                                            except:
                                    
                                                    input[x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1]))
                                                    input[x + 1]= ""
                                    
                    
                    except:
                        print("Next word is not a scale word")
                        input[x] = str(w2n.word_to_num(input[x]))

            for z in tens:
            
                if(input[x] == z):
                    
                    try:
                        res = w2n.word_to_num(input[x+1])

                        for b in units:

                            if(str(input[x+1]) == b):
                    
                              
                                    input [x] = str(w2n.word_to_num(input[x]) + w2n.word_to_num(input[x+1]))
                                    input[x + 1]= ""

                                    
                                    for c in scales:
                                        
                                        if((str(input[x+2])) == c):
                                            
                                            try:
                                                    result = w2n.word_to_num(input[x+3])
                                                    input [x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+2])* w2n.word_to_num(input[x+3]))
                                                    input[x + 2]= ""
                                                    input[x + 3]= ""
                                            except:
                                    
                                                    input[x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+2]))
                                                    input[x + 2]= ""
                                    
                                        

                        
                        
                        
                        for d in scales:
 
                            if((str(input[x+1])) == d):
                                            
                                            try:
                                                    result = w2n.word_to_num(input[x+2])
                                                    input [x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1])* w2n.word_to_num(input[x+2]))
                                                    input[x + 1]= ""
                                                    input[x + 2]= ""
                                            except:
                                    
                                                    input[x] = str(w2n.word_to_num(input[x]) * w2n.word_to_num(input[x+1]))
                                                    input[x + 1]= ""
                                    
                                        
                            
                        
                    except:
                        
                            print("Next word is not a number word")
                            input [x] = str(w2n.word_to_num(input[x]))
                            
    
    

        index1 = 0
        value1 = 0
        index2 = 0
        value2 = 0
        value3 = 0   
        
        
        
        for x in range(len(input)):

            if(str(input[x]) == "and"):
                index1=x
                input[x] = ""
                print(index1)
                
                

                for y in range(0,index1):

                    if(input[y].isnumeric()):
                        value1 = int(str(input[y]))
                        index2 = y
                        print(value1)
                        

                        for z in range(index1,len(input)):
                            if(input[z].isnumeric()):
                                value2 = int(str(input[z]))
                                input[z] = ""
                                print(value2)

        value3 = value1 + value2
        input[index2] = str(value3)

        self.input = self.array2String(input)

        return

    # Remove all numeric characters. - Kishore
    def removeNumbers(self):
        self.input = ''.join([i for i in self.input if not i.isdigit()])
        self.input = (self.input).replace("_", " ")
        return


