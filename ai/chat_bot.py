# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor
from data_post_processor import DataPostProcessor
from teenager import Teenager
from young_adult import YoungAdult
from adult import Adult
from ai_brain import AI
from apscheduler.schedulers.background import BackgroundScheduler

import random, json, os

end = False

# Takes input from commandline, processes it, displays processed output via commandline
def terminalMode():
    # Simple bit of beautifying for our command-line output
    c_background    = "\033[44m"
    c_blue          = "\033[94m"
    c_green         = "\033[92m"
    c_red           = "\033[91m"
    c_close         = "\033[0m"

    # Set up our timer
    timer = BackgroundScheduler({"apscheduler.timezone": "Europe/Dublin"})
    accepted_timer = False

    # Small bit of starting text to introduce the user
    startingText = ["Ask a question, and see how our AI responds.",
    "Please ensure queries have more than three words.",
    "You will have 60 seconds upon entering your first query to make further queries.",
    "The program will wait for your last query before exiting."]
    print(c_green + "\n".join(startingText) + c_close)

    # The timer feature is optional over the command line because it will be implemented by the UI team
    print(c_background + "Do you wish to enable the on-minute timer? (y/n)" + c_close)
    userInput = input()
    if userInput == "y" or userInput == "Y":
        timer.add_job(endProgram, "interval", minutes=1)
        accepted_timer = True

    print(c_background + "Enter the input, or enter 'exit' to end:" + c_close)
    personality = None

    # Retrieve a name
    name = naming()

    # Personality is randomly assigned between teenager, young adult and adult with a random name each time
    perNum = random.randint(1, 3)
    if perNum == 1:
        personality = Teenager(name)
    elif perNum == 2:
        personality = YoungAdult(name)
    else:
        personality = Adult(name)

    # Initialise the ai
    ai = AI()
    ai.initialise(name)
    # Initialise the pre-processor
    preProcessor = DataPreProcessor("")
    # Initialise the post-processor with the personality
    postProcessor = DataPostProcessor(personality)

    # Our input/feedback loop, starting our timer on its initial run
    initial = True
    global end
    while end is False:
        # Start the timer after the first user input if it was accepted
        if initial and accepted_timer:
            timer.start()
        elif not initial:
            print(c_background + "Enter another input:" + c_close)
        initial = False
        # Take the user input
        userInput = input()
        # Exit on 'exit'
        if(userInput == "exit"):
            break
        # Ensure input string is long enough if the terminal is being used
        if preProcessor.processInput(userInput) is not False:
            # Determine our input - whether an error or a valid query
            output = arrangeResp(preProcessor.input, preProcessor, ai)
            # Post-processing of data
            output = postProcessor.postProcess(output)
            # Provide result to the user
            print(c_blue + output + c_close)
        else:
            # Handle queries that are too short
            print(c_red + "The input string must have a minimum of three words!" + c_close)
    # Terminate the program
    print(c_green + "Program exited." + c_close)

def serviceMode():
    # Initialise the AI
    ai = AI()
    ai.initialise("")
    # Initialise the pre-processor
    preProcessor = DataPreProcessor("")
    # Create a previous input to track new questions
    pInput = ""
    # The program will only exit when it recieves a deliberate 'exit' message
    loop = True
    while loop:
        # Check if the file exists
        path = str(os.getcwd()) + "/input.txt"
        if os.path.isfile(path):
            # Read our input from the file
            input_file = open("input.txt", "r")
            # Clean our input
            preProcessor.processInput(input_file.read())
            input = str(preProcessor.input.strip())
            # Exit on 'exit'
            if input == "exit":
                loop = False
            elif input != pInput:
                pInput = input
                # Write the the output back to a different file
                output_file = open("output.txt", "w")
                output = arrangeResp(input, preProcessor, ai)
                output_file.write(output)
                output_file.close()

def arrangeResp(input, preProcessor, ai):
    # This is passed to the model
    response = ai.respond(input, 1)
    # Receive response from the model
    response = preProcessor.array2String(response)
    return response

def naming():
    # Random name generator
    with open("data/names.txt") as word_file:
        names = word_file.read().split()
        name = random.choice(names)
    return name

def endProgram():
    # This exists to allow our timer to end the program
    global end
    end = True
    return

# This function dictates which mode to operate the program in
# For individual use over the command line, un-comment terminalMode()
# For use as a service in the integrated product, un-comment serviceMode()
if __name__ == '__main__':
    if os.getenv("MODE", 0) == 0:
        terminalMode()
    else:
        serviceMode()
