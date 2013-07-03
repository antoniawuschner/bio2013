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
    '''
    adds two strings together
    '''
    return a + b
    
def getCharAt(string, index):
    '''
    returns the character at an index in a string
    '''
    return string[index]
  
def buildList(a, b):
    '''
    makes a list of all the values in between 2 parameters
    '''
    if a<b:
        return range(a,(b+1))
    else:
        c = b
        d = a + 1
        list = range(c,d)
        list.reverse()
        return list
        
def buildDictionary(a):
     '''
     makes a dictionary from an inputed list
     '''
     dictionary = {}
     for number in a:
        dictionary [number] = 1
     return dictionary  

def branch(value):
    '''
    tells if a value is postive, negative, or zero
    '''
    if value == 0:
        return "It's zero"
    elif value>0:
        return "It's positive"
    else:
        return "It's negative"  
    
def forExample(a):
    ord(a)

def isLessThan8(value):
    '''
    tells if the value is less than 8
    '''
    return value<8

def union (a,b):
    '''
    merges two sets
    '''
    return set (set(a)|set(b))
    
class Circle(object):
    
    def __init__(self, center, radius):
       '''
       circle constructor
       '''
       self.center = center
       self.radius = radius 
       
    def getRadius(self):
        '''
        returns the radius of a circle
        '''
        return self.radius
        
    def getCenter(self):
        '''
        returns the center of a circle
        '''
        return self.center  
        
    def getArea(self):
        '''
        calculates the area of a circle
        '''
        return self.radius**2 * math.pi
       
    def buildConcentric(self):
        '''
        creates a concentric circle object
        '''
        return Circle(self, self.getCenter(), (self.getRadius()+4))
        
    def __eq__(self, other):
        '''
        checks if two circles are equal
        '''
        return self.getCenter() == other.getCenter() and self.getRadius() == other.getRadius()
        
    def __ne__(self, other):
        '''
        checks if two circles are not equal
        '''
        return not self.__eq__(other)
         


class Sphere(object):
    
    def __init__(self, center, radius):
        '''
        creates sphere object
        '''
        self.center = center
        self.radius = radius
        
    def getRadius(self):
        '''
        returns the radius of the sphere
        '''
        return self.radius
        
    def getSurfaceArea(self):
        '''
        returns the Surface Area of a sphere
        '''
        return math.pi*4*self.getRadius()**2
        
    def getVolume(self):
        '''
        returns the volume of a sphere
        '''
        return math.pi*(4./3)*self.getRadius()**3
    