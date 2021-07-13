import math
def sieve(num):
    if num <= 2:
        return False
    else:
        highestFactor = int(math.sqrt(num))
        factors = []
        for i in range(2, num + 1):
            if i <= highestFactor or i == num:
                for j in factors:
                    if i % j == 0:
                        break
                else:
                    factors.append(i)
        lastNumber = factors.pop()
        return lastNumber == num

sieve(12)