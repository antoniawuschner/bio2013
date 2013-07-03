import math

def FourierSequence(k, n, numbers):
    total = []
    for x in range(0, len(numbers)):
        sum = 0
        for number in range(0, len(numbers)):
            a = numbers[number]
            b = (-1j * 2 * math.pi * k * n)
            c = float(len(numbers))
            d = b/c
            e = math.e ** d
            sum = sum + a * e
            print x,number
        total.append(sum)
    return total
    