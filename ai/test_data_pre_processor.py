# Class worked on by: Claire, Diego, Luiz Fellipe
import unittest
from data_pre_processor import DataPreProcessor

class TestDataPreProcessor(unittest.TestCase):#pip3 install -U -r requirements.txt

    # Test convert accented chars function
    def test_ConvertChar(self):  
        testInput = "æ"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, "a")

        testInput = "je ètais"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, "je etais")

        testInput = "í"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, "i") 

        testInput = "Ø"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput,"o") 
       
        testInput = "Ùaemd"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, "uaemd") 

        testInput = "ůűų or ŷÝŸ"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput,"uuu or yyy") 



    # Test convert number-words to digits
    def test_NumWordToDigit(self):
        testInput = "fsd"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput, "fsd")

        testInput = "one.two"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput, "one.two")

        testInput = "one"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput, "") 

        testInput = "one two"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput," ") 
       
        testInput = "twelve"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput, "") 

        testInput = "one or three"
        preProcessor = DataPreProcessor(testInput)
        preProcessor.removeNumWords()
        testInput = preProcessor.input
        self.assertEqual(testInput," or ") 


if __name__ == "__main__":
    unittest.main()