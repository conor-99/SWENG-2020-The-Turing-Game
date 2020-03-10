# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor
from teenager import Teenager
from young_adult import YoungAdult
from adult import Adult
from data_post_processor import DataPostProcessor
from ai_brain import AI

import random

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    print('\033[1m' + "Enter the input, or enter 'exit' to end:" + '\033[0m')

    personality = None

    # Personality is randomly assigned between teenager, young adult and adult with a random name each time.
    perNum = random.randint(1, 3)
    if perNum == 1:
        personality = Teenager("Jane Doe")
    elif perNum == 2:
        personality = YoungAdult("James Doe")
    else:
        personality = Adult("Janet Doe")

    while(1):
        userInput = input()

        # exit on 'exit'.
        if(userInput == "exit"):
            break

        output = arrangeResp(userInput, personality)

        print('\033[94m' + "--> " + str(output) + '\033[0m')
        print('\033[1m' + "Enter another input:" + '\033[0m')
    print('\033[92m' + "Program exited." + '\033[0m')

def arrangeResp(userInput, personality):
    #Creating our AI
    ai = AI("James")
    # Where output is the processed output.
    preProcessor = DataPreProcessor(userInput)
    preProcessor.processInput()

    # This is passed to the model.
    processedInput = preProcessor.input
    # Receive response from the model
    response = ai.respond(processedInput, 1)
    response = preProcessor.array2String(response)
    # postProcessor = DataPostProcessor(response, personality)

    return response

if __name__ == '__main__':
    main()
