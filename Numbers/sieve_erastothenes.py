#program to find number of  primes less than given number n

class Solution(object):
    def number__of__primes(self, n):
        if n <= 1:
            return 0

        primeArr = [True] * n
        primeArr[0] = False
        primeArr[1] = False
        primes = 0
        for i in range(n):
            if primeArr[i]:
                primes += 1
                for j in range( 2*i, n, i ):
                    primeArr[j] = False

        return primes

    number__of__primes( object, 10000 )