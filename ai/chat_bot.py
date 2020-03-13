# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor
from teenager import Teenager
from young_adult import YoungAdult
from adult import Adult
from data_post_processor import DataPostProcessor
from ai_brain import AI
from apscheduler.schedulers.background import BackgroundScheduler

import random

end = False

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # This will be an environment variable later
    terminalMode = True
    # Simple bit of beautifying for our command-line output.
    c_background   = ""
    c_blue         = ""
    c_green        = ""
    c_red          = ""
    c_close        = ""
    # Certain aspects of this program will only exist on the commandline.
    if terminalMode:
        # Set up our timer
        timer = BackgroundScheduler()
        timer.add_job(endProgram, "interval", minutes=1)
        c_background    = "\033[44m"
        c_blue          = "\033[94m"
        c_green         = "\033[92m"
        c_red           = "\033[91m"
        c_close         = "\033[0m"
        # Small bit of starting text to introduce the user.
        startingText = ["Ask a question, and see how our AI responds.",
        "Please ensure queries have more than three words.",
        "You will have 60 seconds upon entering your first query to make further queries.",
        "The program will wait for your last query before exiting."]
        print(c_green + "\n".join(startingText) + c_close)

        # Where input is user input from commandline.
        print(c_background + "Enter the input, or enter 'exit' to end:" + c_close)

    personality = None

    # Random name generator
    with open("data/names.txt") as word_file:
        names = word_file.read().split()
        name = random.choice(names)

    # Personality is randomly assigned between teenager, young adult and adult with a random name each time.
    perNum = random.randint(1, 3)
    if perNum == 1:
        personality = Teenager(name)
    elif perNum == 2:
        personality = YoungAdult(name)
    else:
        personality = Adult(name)

    # Our input/feedback loop, starting our timer on its initial run.
    initial = True
    global end
    while(not end):
        if terminalMode:
            userInput = input()
            # Start the timer after the first user input.
            if initial:
                timer.start()
                initial = False
            # Exit on 'exit'.
            if(userInput == "exit"):
                break
            # Determine our input, whether an error or a valid query.
            output = arrangeResp(userInput, personality)
            # Handle queries that are too short.
            if output == False:
                print(c_red + "The input string must have a minimum of three words!" + c_close)
            else:
                print(c_blue + output + c_close)
            print(c_background + "Enter another input:" + c_close)
    if terminalMode:
        print(c_green + "Program exited." + c_close)

def arrangeResp(userInput, personality):
    # Creating our AI.
    ai = AI(personality.name)
    # Where output is the processed output.
    preProcessor = DataPreProcessor(userInput)
    # Was the query too short for the AI, if so, exit.
    if preProcessor.processInput() == False:
        return False
    # This is passed to the model.
    processedInput = preProcessor.input
    # Receive response from the model.
    response = ai.respond(processedInput, 1)
    response = preProcessor.array2String(response)
    postProcessor = DataPostProcessor(response, personality)
    postProcessor.postProcess()
    return response

def endProgram():
    global end
    end = True
    return

if __name__ == '__main__':
    main()