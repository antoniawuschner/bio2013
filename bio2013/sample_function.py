import math

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
  
    def practiceFunction(x,y):
        FourierData = []
        for i in range(x,y):
            FourierData.append(math.sin(i) * math.exp(-i))
        return FourierData

    def sinFunctionData(self,x,y):
        FourierData = []
        for i in range(x,y):
            FourierData.append(self.calcOnePoint(i))
        return FourierData

    def calcOnePoint(self,i):
        point = self.getA() * math.sin((i * self.getW()) + self.getOffset()) * math.exp (-i * self.getT())
        return point
        
        