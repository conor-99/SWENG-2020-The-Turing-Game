# Class worked on by: Claire, Luiz Fellipe

from data_pre_processor import DataPreProcessor

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    print("Enter the input")
    userInput = input()
    preProcessor = DataPreProcessor(userInput)

    # Where output is the processed output.
    preProcessor.processInput()
    output = preProcessor.input
    print(output)

if __name__ == '__main__':
    main()