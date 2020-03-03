# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor
from teenager import Teenager
from data_post_processor import DataPostProcessor

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    print('\033[1m' + "Enter the input, or enter 'exit' to end:" + '\033[0m')

    # This will be randomly assigned between teenager, young adult and adult with a random name each time.
    personality = Teenager("Jane Doe")

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
    # Where output is the processed output.
    preProcessor = DataPreProcessor(userInput)
    preProcessor.processInput()
    
    # This is passed to the model.
    processedInput = preProcessor.input

    # processedInput = modelOutput

    # Output of model is passed to data post processor.
    # postProcessor = DataPostProcessor(processedInput, personality)

    return processedInput





if __name__ == '__main__':
    main()
