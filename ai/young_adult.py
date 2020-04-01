# Class worked on by: Claire
import random
from personality import Personality
from data_pre_processor import DataPreProcessor

class YoungAdult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(22, 28)
        self.probSpellingMistake = random.randint(2,5)
    
    def addPersonality(self, input):
        output = self.shortenWords(input)
        return output

    # You -> u for instance, more likely to be commonly appropriate. Needs to return a string. - Kishore
    def shortenWords(self, input):
        shortWords = {
            'for your information' : 'fyi',
            'okay' : 'kk',
            'ok':'kk',
            'easy' : 'ez',
            'see you' : 'cya',
            'because' : 'cuz',
            'very' : 'v',
            'to be honest' : 'tbh',
            'oh my god' : 'OMG',
            'boyfriend' : 'bf',
            'girlfriend' : 'gf',
            'awesome' : 'cool',
            'in trouble' : 'screwed',
            }        
        preProcessor = DataPreProcessor(input) 
        input = preProcessor.string2Array(input)    
        for x in range(0,len(input)):
            for y in shortWords:
                if(str(input[x]) == y):
                    input[x] = shortWords[y]
        input = preProcessor.array2String(input)               
    
        return input
    
    # Add appropriate emjois - Luiz Fellipe
    def addEmojis(self, input):

        if input.find('sad')!= -1:
            index = input.find('sad')
            length = len('sad')
            output_line = input[:index+length] + ' \U0001F625' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('happy')!= -1:
            index = input.find('happy')
            length = len('happy')
            output_line = input[:index+length] + ' \U0001F603' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('funny')!= -1:
            index = input.find('funny')
            length = len('funny')
            output_line = input[:index+length] + ' \U0001F602' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('love')!= -1:
            index = input.find('love')
            length = len('love')
            output_line = input[:index+length] + ' \U0001F60D' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('star')!= -1:
            index = input.find('star')
            length = len('star')
            output_line = input[:index+length] + ' \U0001F929' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('good night')!= -1:
            index = input.find('good night')
            length = len('good night')
            output_line = input[:index+length] + ' \U0001F634' + input[index+length:]
            print(output_line)
            return output_line
        elif input.find('angry')!= -1:
            index = input.find('angry')
            length = len('angry')
            output_line = input[:index+length] + ' \U0001F621' + input[index+length:]
            print(output_line)
            return output_line
        
        return input