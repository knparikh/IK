#!/bin/python3

import os
import sys
import math


# Compute F(pascal triangle array), where Pascal's triangle is
# triangle of binomial coefficients:
# P(i, j) = i! / (i-j)!* j!, where i is line number, j is col number
# Example n = 4, pascal triangle is:
# 1
# 1  1
# 1  2  1
# 1  3  3  1
# 1  4  6  4 1
# 1  5 10 10 5 1
# Compute F(pascaltriangle) = Summation over all i (Summation over all j (j+1)*array[i][j] + (j+1)) % (10^9 + 7), 
# where 0<=i<n and 0<=j<=i
# 
# Binomial coefficient(n, k) = n!/(n-k)!*k!
# To compute for each n,k use previous result from same line
# Bin coeff (n, k-1) = n!/(n-k+1)! * (k-1)!
# Bin coeff(n, k) = 1 if k = 0 else Bin coeff(n, k-1) * (n-k+1)/ k
def findFofPascalTriangle(n):
    sum = 0
    for i in range(0, n, 1):
        prev = 1
        for j in range(0, i+1, 1):
            if j == 0:
                coeff = prev
            else:
                coeff = prev * (i - j + 1) / j
            print(coeff)
            sum += ((i+1) * coeff) + (j+1)
            prev = coeff
        print("\n")

    return int(sum % (math.pow(10, 9) + 7))

if __name__ == '__main__':

    n = int(input())

    res = findFofPascalTriangle(n)

    print(res)


if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    res = findFofPascalTriangle(n)

    fptr.write(str(res) + '\n')

    fptr.close()

