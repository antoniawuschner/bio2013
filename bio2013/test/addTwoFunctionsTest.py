from .. import addTwoFunctions as a
import unittest

class TestFirst(unittest.TestCase):
     
    def testaddTwoFunctions(self):
        self.assertEqual(a.addTwoFunctions(math.sin,math.cos,0,1),[1,1.017])