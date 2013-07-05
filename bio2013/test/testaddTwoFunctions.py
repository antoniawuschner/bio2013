from .. import addTwoFunctions as a
import unittest
import math

class TestFirst(unittest.TestCase):
     
    def testaddTwoFunctions(self):
        self.assertEqual(a.addTwoFunctions(math.sin,math.cos,0,2),[1.0,1.3817732906760363])