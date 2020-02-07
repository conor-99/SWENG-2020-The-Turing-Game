# Class worked on by: Claire, Luiz Fellipe

from data_pre_processor import DataPreProcessor

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # Where input is user input from commandline.
    preProcessor = DataPreProcessor(input)

    # Where output is the processed output.
    output = preProcessor.processInput()


if __name__ == '__main__':
    main()