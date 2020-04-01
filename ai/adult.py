# Class worked on by: Claire
import random
from personality import Personality

class Adult(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(29, 40)
        self.probSpellingMistake = random.randint(5,7)
    
    def addPersonality(self, input):
        output = self.addPunctuation(input)
        return output

    # The returned string from the AI model does not have any punctuation. 
    # This function needs to add punction to that string and return it. - Diego
    def addPunctuation(self, input):
        #Sentence Openers nn
        input = input.replace("hello", "hello,")
        input = input.replace("hi", "hi!")
        input = input.replace("heya", "heya!")
        input = input.replace("hey", "hey,")
        input = input.replace("greetings", "greetings,")
        input = input.replace("good morning", "good morning,")
        input = input.replace("good evening", "good evening,")
        input = input.replace("good afternoon", "good afternoon!")
    

        #Words ending in nt 
        input = input.replace("isnt", "isn't")
        input = input.replace("cant", "can't")
        input = input.replace("wont" , "won't")
        input = input.replace("dont" , "don't")
        input = input.replace("would", "wouldn't")
        input = input.replace("hadnt", "hadn't")
        input = input.replace("aint", "ain't")
        input = input.replace("arent", "aren't")
        input = input.replace("didnt", "didn't")
        input = input.replace("doesnt" , "doesn't")
        input = input.replace("dont" , "don't")
        input = input.replace("dont", "don't")
        input = input.replace("hasnt", "hasn't")
        input = input.replace("shoudlnt", "shouldn't")
        input = input.replace("couldnt", "couldn't")

        input = input.replace("wasnt", "wasn't")
        input = input.replace("werent" , "were't")
        input = input.replace("wouldnt" , "wouldn't")

        #Questions
        q1 = "what"
        q2 = "when"
        q3 = "where"
        q4 = "which"
        q5 = "who"
        q6 = "whom"
        q7 = "whose"
        q8 = "why"
        q9 = "how"

        if (input.count(q1) == 1 or input.count(q2) == 1 or input.count(q3) == 1 
        or input.count(q4) == 1 or input.count(q5) == 1 or input.count(q6) == 1 
        or input.count(q7) == 1 or input.count(q8) == 1 or input.count(q9) == 1) : input = input + "?"

        else: input = input + "."


        #Other
        input = input.replace("however", "however,")
        input = input.replace("ill" , "i'll")
        input = input.replace("im", "i'm")
        return input