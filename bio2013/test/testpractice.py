from .. import classesanddatums as c
import unittest



class TestStuff(unittest.TestCase):
    
    def testConcatenate(self):
        self.assertEqual('abcdef', c.concatenate('abc', 'def'))
    
    def testGetCharAt(self):
        self.assertEqual('c', c.getCharAt('abcdef', 2))
        self.assertEqual('e', c.getCharAt('abcdef', 4))
    
    def testBranch(self):
        self.assertEqual(branch(0), "it's zero")
        self.assertEqual(branch(-18), "it's negative")
        self.assertEqual(branch(72), "it's positive!!!1one")

    def testForExample(self):
        self.assertEqual(97, c.forExample('?a9\n'))
        self.assertEqual(34952, c.forExample(u'\u1234\u8888q'))
    
    def testCreateList(self):
        self.assertEqual([1,2,3,4,5], c.buildList(1, 5))
        self.assertEqual([3,2,1,0,-1], c.buildList(3, -1))
    
    def testCreateDictionary(self):
        self.assertEqual({'a': 1, 'b': 1}, c.buildDictionary(['a', 'b']))
        self.assertEqual({}, c.buildDictionary(['a', 'b']))
        self.assertEqual({1: 1, 'q': 1, 'd': 1}, c.buildDictionary([1, 'q', 'd']))
    
    def testUnion(self):
        self.assertEqual(set([]), c.union(set([]), set([])))
        self.assertEqual(set([1, 18, 72]), c.union(set([1, 72]), set([18, 72])))
    
    def testPredicate(self):
        self.assertFalse(c.isLessThan8(9))
        self.assertTrue(c.isLessThan8(4))
        
        
class TestClasses(unittest.TestCase):
    
    def testCircleEquality(self):
        self.assertEqual(c.Circle((2, 3), 22), c.Circle((2, 3), 22))
    
    def testCircleArea(self):
        self.assertAlmostEqual(50.2654824574, c.Circle((2, 3), 4).getArea())
    
    def testSphereSurfaceArea(self):
        self.assertAlmostEqual(804.247719318, c.Sphere((0, 0, 0), 8))
    
    def testSphereSurfaceArea(self):
        self.assertAlmostEqual(2144.660584850, c.Sphere((0, 0, 0), 8))
