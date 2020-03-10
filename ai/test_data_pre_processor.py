# Class worked on by: Claire, Diego, Luiz Fellipe
import unittest
from data_pre_processor import DataPreProcessor

class TestDataPreProcessor(unittest.TestCase):#pip3 install -U -r requirements.txt

    # Test convert accented chars function - Diego 

    def test_ConvertChar(self):  
        testInput = 'æ'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'a')

        testInput = 'je ètais'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'je etais')

        testInput = 'í'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'i') 

        testInput = 'Ø'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput,'o') 
       
        testInput = 'Ùaemd'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'uaemd') 

        testInput = 'ůűų or ŷÝŸ'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertAccentedCharsToAscii()
        testInput = preProcessor.input
        self.assertEqual(testInput,'uuu or yyy') 



    # Test convert number word to digit - Luiz Fellipe
    def test_NumWordToDigit(self):
        testInput = 'fsd'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'fsd')

        # FAILS THIS TEST
        testInput = 'one.two'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        print (f"{testInput} : testing input")
        self.assertEqual(testInput, '1.2')

        testInput = 'one'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput, '1') 

        # FAILS THIS TEST
        testInput = 'one two'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput,'1 2') 
       
        testInput = 'twelve'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput, '12') 

        testInput = 'one or three'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput,'1 or 3') 


if __name__ == '__main__':
    unittest.main()