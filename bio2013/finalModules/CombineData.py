import math

def CombineData(list1,list2):
    addedValues = [x+y for (x,y) in zip(list1,list2)]
    return addedValues