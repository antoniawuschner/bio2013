from .. import first
import unittest



class TestFirst(unittest.TestCase):
     

    def testSum(self):
        result = first.sum1([1,2,3])
        self.assertEqual(6,result)
    def testSum2(self):
    	self.assertEqual(6,first.sum1([0.5,2.5,3]))
        
    def testBaseCase(self):
        self.assertEqual(0,first.sum1([]))
