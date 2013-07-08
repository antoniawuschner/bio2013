import math

def addTwoFunctions(function1,function2,x,y):
    a = map(function1,range(x,y))
    b = map(function2,range(x,y))
    return addTwoLists(a,b)
    
def addTwoLists(list1,list2):
    addedValues = map(addXandY,zip(list1,list2))
    return addedValues

def addXandY(pair):
    sum = pair[0] + pair[1]
    return sum
    
def addFunctions(function1,function2,x,y):
    a = [function1(i) for i in range(x,y)]
    b = [function2(i) for i in range(x,y)]
    return addTwoListsComprehension(a,b)
    
def addTwoListsComprehension(list1,list2):
    addedValues = [x+y for (x,y) in zip(list1,list2)]
    return addedValues
    
def addLists(list)
    for (i%2
    finallist = [x+y for (x,y) in zip(list1,list2)]