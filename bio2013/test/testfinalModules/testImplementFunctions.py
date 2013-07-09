from ...finalModules import ImplementFunctions as imp
import unittest
import math


class TestIF(unittest.TestCase):
    
    def testSin(self):
        f = imp.sinFunction(1, 1, 0, 0) # exponential time decay 0 -- pure sine wave
        self.assertAlmostEqual(f(0), 0)
        self.assertAlmostEqual(f(math.pi / 2.), 1)
        self.assertAlmostEqual(f(math.pi), 0)
        self.assertAlmostEqual(f(3 * math.pi / 2.), -1)
    
    def testSinAmplitude(self):
        f = imp.sinFunction(4, 1, 0, 0)
        self.assertAlmostEqual(f(0), 0)
        self.assertAlmostEqual(f(math.pi / 2.), 4)
        self.assertAlmostEqual(f(math.pi), 0)
        self.assertAlmostEqual(f(3 * math.pi / 2.), -4)
    
    def testSinPeriod(self):
        f = imp.sinFunction(4, 3, 0, 0)
        self.assertAlmostEqual(f(0), 0)
        self.assertAlmostEqual(f(math.pi / 6.), 4)
        self.assertAlmostEqual(f(math.pi / 3.), 0)
        self.assertAlmostEqual(f(math.pi / 2.), -4)
    
    def testDecay(self):
        f = imp.sinFunction(1, 1, 0, 1)
        def formula(x):
            return math.sin(x) * math.e ** -x
        v1, v2, v3 = map(formula, [math.pi / 6., math.pi / 2., 3 * math.pi / 2.])
        self.assertAlmostEqual(f(math.pi / 6.), v1)
        self.assertAlmostEqual(f(math.pi / 2.), v2)
        self.assertAlmostEqual(f(3 * math.pi / 2.), v3)
