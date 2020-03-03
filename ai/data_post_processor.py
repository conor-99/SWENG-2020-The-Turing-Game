# Class worked on by: Claire
from personality import Personality

class DataPostProcessor:

    def __init__(self, input, personality):
        self.input = input
        self.personality = personality

    def postProcess(self):
        self.personality.addPersonality(self.input)
