# Calculate all prime factors of a number and then judge wether it is ugly
# i.e factor only of 2 and 3

import math

class Solution(object):
    def is__ugly(self, num):
        if num <= 0:
            return False

        primes = []
        if num%2 == 0:
            num = num/2
            primes.append(2)
        for i in range( 3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                primes.append(int(i))
                num = num / i
        if num > 2:
            primes.append(int(num))
        print(primes)
        for index, k in enumerate(primes):
            if primes[index] == 2 or primes[index] == 3 or primes[index] == 5:
                continue
            else:
                return False
        return True
    is__ugly(object, 46)
