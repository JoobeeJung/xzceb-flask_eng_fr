import unittest
from translator import frenchToEnglish, englishToFrench

class TestNull(unittest.TestCase): 
    def test_frenchToEnglish_null(self): 
        self.assertEqual(frenchToEnglish(''), '')

    def test_englishToFrench_null(self): 
        self.assertEqual(englishToFrench(''), '' )

class TestNotEqual(unittest.TestCase): 
    def test_frenchToEnglish_notEqual(self): 
        self.assertNotEqual('Hello', 'Bonjour')  

    def test_englishToFrench_notEqual(self): 
        self.assertNotEqual('Bonjour', 'Hello') 

unittest.main()