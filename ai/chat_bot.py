# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    print('\033[1m' + "Enter the input, or enter 'exit' to end:" + '\033[0m')
    while(1):
        userInput = input()
        # exit on 'exit'
        if(userInput == "exit"):
            break
        preProcessor = DataPreProcessor(userInput)

        # Where output is the processed output.
        preProcessor.processInput()
        output = preProcessor.input
        print('\033[94m' + "--> " + str(output) + '\033[0m')
        print('\033[1m' + "Enter another input:" + '\033[0m')
    print('\033[92m' + "Program exited." + '\033[0m')

if __name__ == '__main__':
    main()
