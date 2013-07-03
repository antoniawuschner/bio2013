'''
this is a doc comment
'''
import math

def void():
    '''
    this is a function's doc comment
    '''
    pass


def concatenate(a, b):
    answer = ""
    answer = a + b
    return answer
    


def getCharAt(string, index):
    return string[index]
  
def buildList(a, b):
    if a<b:
       return range(a,(b+1))
    else:
        c = b
        d = a+1
        list = range(c,d)
        list.reverse()
        return list
def buildDictionary(a):
     dictionary = {}
     for number in a:
        dictionary.update({number:1})
     return dictionary  

def branch(value):
    if value == 0:
        return "It's zero"
    elif value>0:
        return "It's positive"
    else:
        return "It's negative"  
    

def forExample(a):
    ord(a)

def isLessThan8(value):
    if value<8:
        return True
    else:
        return False  

def union (a,b):
   return set (set(a)|set(b))
    
class Circle(object):
    
    def __init__(self, center, radius):
       self.center = center
       self.radius = radius 
    def getRadius(self):
        return self.radius
    def getCenter(self):
        return self.center  
    def getArea(self):
       return self.radius**2 * math.pi
    def buildConcentric(self):
        return Circle(self, self.getCenter(), (self.getRadius()+4))
    def __eq__(self, other):
        if self.getCenter() == other.getCenter():
            if self.getRadius() == other.getRadius():
                return "true"
        else:
            return "false"
    def __ne__(self, other):
        raise ValueError('unimplemented')


class Sphere(object):
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def getRadius(self):
        return self.radius
    def getSurfaceArea(self):
        return math.pi*4*self.getRadius()**2
    def getVolume(self):
        return math.pi*(4./3)*self.getRadius()**3
    