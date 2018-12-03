#!/usr/bin/env python
import CharacterReplacement as script1
import StringFormat as script2

import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp (self):
        self.script1Test = script1.rot13
        self.script2Test = script2.format_duration

        self.script1Param1 = "Test"
        self.script2Param1 = 1232323

        self.script1Result = "Grfg"
        self.script2Result = "14 days, 6 hours, 18 minutes and 43 seconds"

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_script1(self):
        self.assertEqual(self.script1Test(self.script1Param1), self.script1Result)

    def test_script2(self):
        self.assertEqual(self.script2Test(self.script2Param1), self.script2Result)

    def test_script3_raisesException(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(self.script3Test(self.script3Param1), self.script3Result)
            #raises an exception because script3 does not exist

    def tearDown(self):
        pass

if __name__ == "__main__":
    #assert script1.rot13("Test") == "Grfg", "Oh no! script 1 failed!"

    #assert script2.format_duration (1232323) == "14 days, 6 hours, 18 minutes and 43 seconds", "Oh no! script 2 failed!"

    unittest.main()

