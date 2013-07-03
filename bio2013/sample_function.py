import math

def practiceFunction(x,y):
    FourierData = []
    for i in range(x,y):
        FourierData.append(math.sin(i) * math.exp(-i))
    return FourierData

def sinFunction(x,y,a,w,offset,t):
    FourierData = []
    for i in range(x,y):
        FourierData.append(calcOnePoint(a,w,offset,t))
    return FourierData

def calcOnePoint(a,w,offset,t)
    point = a * math.sin((i * w) + offset) * math.exp (-i * t)
    return point