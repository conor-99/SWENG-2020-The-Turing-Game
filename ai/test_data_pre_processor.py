# Class worked on by: Claire, Diego, Luiz Fellipe
import unittest
from data_pre_processor import DataPreProcessor

class TestDataPreProcessor(unittest.TestCase):

    # Test convert accented chars function - Diego 

    # def test_ConvertChar(self):

    # Test convert number word to digit - Luiz Fellipe
    def test_NumWordToDigit(self):
        
        testInput = 'fsd'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput, 'fsd')

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
        self.assertEqual(testInput,1) 

        testInput = 'one two'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput,'1 2') 
       
        testInput = 'twelve'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput,12) 

        testInput = 'one or three'
        preProcessor = DataPreProcessor(testInput)
        preProcessor.convertNumberWordToDigit()
        testInput = preProcessor.input
        self.assertEqual(testInput,'1 or 3') 


if __name__ == '__main__':
    unittest.main()