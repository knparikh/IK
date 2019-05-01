#!/bin/python3

import os
import sys


# Check for special cases:
# n = 0, 1 ,2 True
# If divisible by 2, 3 return False
# Prime numbers are 6k+-1. Start with k = 1 i.e. compare with 5,7 and go upto sqrt(n)
def is_prime(n):

    if n == 1:
        return 0
    if n == 2:
        return 1


    if (n % 2) == 0 or (n % 3) == 0:
        return 0


    k = 5
    while(k*k <= n):
        if (n % k) == 0 or (n % k+2) == 0:
            return 0
        k = k + 6

    return 1

#XXX TODO  All primes above 3 can be represented as 6k + 1
# Test 2097299

def detect_primes(a):
    out = []

    for i in a:
        out.append(str(is_prime(i)))

    return ''.join(out)


if __name__ == '__main__':

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    res = detect_primes(a)

    print(res)



if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    res = detect_primes(a)

    fptr.write(res + '\n')

    fptr.close()



