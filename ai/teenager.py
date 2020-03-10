# Class worked on by: Claire
import random
import string

from personality import Personality


class Teenager(Personality):

    def __init__(self, name):
        Personality.__init__(self, name)
        self.age = random.randint(13, 21)

    def addPersonality(self, input):
        output = textSubstitution(input)
        return output

    # Add text substitution to the input.
    def textSubstitution(self, input):
        # Shortening words continuously is far more common.
        output = shortenWords(input)

        # Adding spelling mistakes should not happen everytime.
        if random.randint(1, 5) == 1:
            output = addSpellingMistakes(input)
        return output

    # You -> u for instance, more likely to be commonly appropriate. Needs to return a string. - Kishore
    def shortenWords(self, input):
        return

    # Substitute words with common misspellings IF APPROPRIATE. Needs to return a string .- Luiz Fellipe
    def addSpellingMistakes(self, input):
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
    
        probOfTypoArray = []
        probOfTypo = int(prob * 100)

        returnText = input
        while input == returnText:
            returnText = ''
            for letter in input:
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

        return returnText

