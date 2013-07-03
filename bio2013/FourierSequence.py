import math

def FourierSequence(numbers):
    total = []
    for x in range(0, len(numbers)):
        sum = 0
        for number in range(0, len(numbers)):
            a = numbers[number]
            b = (-1j * 2 * math.pi * x * number)
            c = float(len(numbers))
            d = b/c
            e = math.e ** d
            sum = sum + a * e
            print x,number
        total.append(sum)
    return total
    