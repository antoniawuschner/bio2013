import math

def practiceFunction(x,y):
    FourierData = []
    for i in range(x,y):
        FourierData.append(math.sin(i) * math.exp(-i))
    return FourierData
    