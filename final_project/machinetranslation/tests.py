import unittest
from translator import french_to_english, english_to_french

class TestNull(unittest.TestCase): 
    def test_frenchToEnglish_null(self): 
        self.assertEqual(french_to_english(''), '')

    def test_englishToFrench_null(self): 
        self.assertEqual(english_to_french(''), '' )

class TestNotEqual(unittest.TestCase): 
    def test_frenchToEnglish_notEqual(self): 
        self.assertNotEqual('Hello', 'Bonjour')  

    def test_englishToFrench_notEqual(self): 
        self.assertNotEqual('Bonjour', 'Hello') 

unittest.main()