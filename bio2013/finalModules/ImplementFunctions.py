import math

def addFunctions(function1,function2,x,y):
    '''
    Takes in two functions and a range of x values and calculates the sum of the two lists of y values for those functions
    Parameters:
    -Function1 and function2 - two functions (ex. math.sin)
    -x-starting value for range
    -y-ending value for range
    
    The addTwoListsComprehension method is called
    '''
    a = [function1(i) for i in range(x,y)]
    b = [function2(i) for i in range(x,y)]
    return addTwoListsComprehension(a,b)
    
class sinFunction(object):

    def __init__(self,a,w,offset,t):
       '''
       sin equation constructor
       Parameters:
       -a - amplitude
       -w - period
       -offset - offset
       -t - time
       '''
       self.a = a
       self.w = w
       self.offset = offset
       self.t = t
       
    def __call__(self,x):
        return self.CalculateOnePoint(x)
    
    def CalculateOnePoint(self,x):
        point = self.a * math.sin((x * self.w) + self.offset) * math.exp (-x * self.t)
        return point