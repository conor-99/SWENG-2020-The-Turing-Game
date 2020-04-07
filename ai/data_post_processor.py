# Class worked on by: Claire, Luiz Fellipe
from personality import Personality
import random

class DataPostProcessor:

    def __init__(self, input, personality):
        self.input = input
        self.personality = personality

    def postProcess(self):
        #self.input = self.personality.addPersonality(self.input)
        if random.randint(1, self.personality.probSpellingMistake) == 1:
            self.addSpellingMistakes()

    # Substitute words with common misspellings IF APPROPRIATE. Needs to return a string.
    def addSpellingMistakes(self):
        prob=0.1
        keyApprox = {}
        
        keyApprox['q'] = "qwasedzx"
        keyApprox['w'] = "wqesadrfcx"
        keyApprox['e'] = "ewrsfdqazxcvgt"
        keyApprox['r'] = "retdgfwsxcvgt"
        keyApprox['t'] = "tryfhgedcvbnju"
        keyApprox['y'] = "ytugjhrfvbnji"
        keyApprox['u'] = "uyihkjtgbnmlo"
        keyApprox['i'] = "iuojlkyhnmlp"
        keyApprox['o'] = "oipklujm"
        keyApprox['p'] = "plo['ik"
        keyApprox['a'] = "aqszwxwdce"
        keyApprox['s'] = "swxadrfv"
        keyApprox['d'] = "decsfaqgbv"
        keyApprox['f'] = "fdgrvwsxyhn"
        keyApprox['g'] = "gtbfhedcyjn"
        keyApprox['h'] = "hyngjfrvkim"
        keyApprox['j'] = "jhknugtblom"
        keyApprox['k'] = "kjlinyhn"
        keyApprox['l'] = "lokmpujn"
        keyApprox['z'] = "zaxsvde"
        keyApprox['x'] = "xzcsdbvfrewq"
        keyApprox['c'] = "cxvdfzswergb"
        keyApprox['v'] = "vcfbgxdertyn"
        keyApprox['b'] = "bvnghcftyun"
        keyApprox['n'] = "nbmhjvgtuik"
        keyApprox['m'] = "mnkjloik"
        keyApprox[' '] = " "
    
        probOfTypo = int(prob * 100)

        returnText = self.input
        while self.input == returnText:
            returnText = ''
            for letter in self.input:
                lcletter = letter.lower()
                if not lcletter in keyApprox.keys():
                    newletter = lcletter
                else:
                    if random.choice(range(0, 1000)) <= probOfTypo:
                        newletter = random.choice(keyApprox[lcletter])
                    else:
                        newletter = lcletter
                # go back to original case
                if not lcletter == letter:
                    newletter = newletter.upper()
                returnText += newletter

        self.input = returnText

        return 