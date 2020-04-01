# Class worked on by: Claire, Luiz Fellipe, Leo
from data_pre_processor import DataPreProcessor
from teenager import Teenager
from young_adult import YoungAdult
from adult import Adult
from data_post_processor import DataPostProcessor
from ai_brain import AI
from apscheduler.schedulers.background import BackgroundScheduler

import random, json

end = False

# Takes input from commandline, processes it, displays processed output via commandline.
def main():
    # This will be an environment variable later
    terminalMode = False
    # Simple bit of beautifying for our command-line output.
    c_background   = ""
    c_blue         = ""
    c_green        = ""
    c_red          = ""
    c_close        = ""
    # Certain aspects of this program will only exist on the commandline.
    if terminalMode:
        # Set up our timer
        timer = BackgroundScheduler({"apscheduler.timezone": "Europe/Dublin"})
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
        else:
            # handle input through a json file
            with open("connect.json") as json_file:
                data = json.load(json_file)
                for i in data["user"]:
                    uuid = i["uuid"]
                    userInput = i["question"]
                    jPersonality = i["personality"]
                    answered = i["answered"]
            # if a personality has been established dont change it
            if jPersonality == "":
                jPersonality = perNum
            # make sure we aren't working on an answered question
            if answered is False:
                dump = {}
                # arrange response json with the output contained
                dump["user"] = []
                dump["user"].append({
                    "uuid" : uuid,
                    "question" : userInput,
                    "personality" : jPersonality,
                    "output" : arrangeResp(userInput, personality),
                    "answered" : "True"
                })
                with open("connect.json", "w") as outfile:
                    json.dump(dump, outfile)
            end = True
    if terminalMode:
        print(c_green + "Program exited." + c_close)

def arrangeResp(userInput, personality):
    # Creating our AI.
    ai = AI(personality.name)
    # Where output is the processed output.
    preProcessor = DataPreProcessor(userInput)
    # Ensure input string is long enough if the terminal is being used
    if preProcessor.processInput() is not True:
        return False
    processedInput = preProcessor.input
    # This is passed to the model.
    response = ai.respond(processedInput, 1)
    # Receive response from the model.
    response = preProcessor.array2String(response)
    # Post-processing of data
    postProcessor = DataPostProcessor(response, personality)
    postProcessor.postProcess()
    return response

def endProgram():
    global end
    end = True
    return

if __name__ == '__main__':
    main()
