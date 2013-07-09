from ... finalModules import CalculateFT as Fourier
import unittest
import math
import numpy as np

class TestFirst(unittest.TestCase):
     
    def testFourierTransform(self):
        a = [ 6.0+0.j,-1.5+0.8660254j,-1.5-0.8660254j]
        b = Fourier.FourierSequence([1,2,3])
        for y in range(0,len(a)):
            self.assertAlmostEqual(a[y],b[y])
        