from .. import sample_function as a
import unittest

class TestFirst(unittest.TestCase):
     
    def testSample(self):
        self.assertEqual(a.practiceFunction(0,1),[0.0])
    
    def testSinFunction(self):
        self.assertEqual(a.sinFunction(0,1,1,1,0,1), [0.0])
    
    def testSinFunction(self):
        self.assertEqual(a.sinFunction(0,1,1,1,0,1), a.practiceFunction(0,1))
        