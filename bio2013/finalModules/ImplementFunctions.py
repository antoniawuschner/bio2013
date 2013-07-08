import math

def addFunctions(function1,function2,x,y):
    a = [function1(i) for i in range(x,y)]
    b = [function2(i) for i in range(x,y)]
    return addTwoListsComprehension(a,b)
    
class sinFunction(object):

    def __init__(self,a,w,offset,t):
       '''
       equation constructor
       '''
       self.a = a
       self.w = w
       self.offset = offset
       self.t = t 
   
    def getA(self):
        return self.a 
    
    def getW(self):
        return self.w 
        
    def getOffset(self):
        return self.offset 
    
    def getT(self):
        return self.t  
  
    