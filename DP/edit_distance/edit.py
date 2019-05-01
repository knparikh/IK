#!/bin/python3

import sys
import os

# Given two words word1 and word2 find minimum number of steps required to convert word1 to word2
# Following operations are permitted:
# 1. Insert a char f(i, j+1)
# 2. Delete a char f(i+1, j)
# 3. Modify a char f(i+1, j+1)
# Recursive formulation:
# f(i, j) : Return # of transformations needed to convert s1 to s2 starting at i and j
#           0 if i == len(s1) and j == len(s2)
#           len(s2) - j if i == len(s1) 
#           len(s1) - i if j == len(s2) 
#           f(i+1, j+1) if s1[i] == s2[j]
#           1 + min(f(i, j+1), f(i+1, j), f(i+1, j+1))
def  levenshteinDistance(strWord1, strWord2):
    s1 = list(strWord1)
    s2 = list(strWord2)

    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1) ]

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i == len(s1) and j == len(s2):
                dp[i][j] = 0
            elif i == len(s1):
                dp[i][j] = len(s2) - j
            elif j == len(s2):
                dp[i][j] = len(s1) - i
            elif s1[i] == s2[j]:  # Chars match, no operation needed to match
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]


if __name__ == "__main__":

    _strWord1 = str(input())

    _strWord2 = str(input())

    res = levenshteinDistance(_strWord1, _strWord2);
    print(str(res))


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
        

    _strWord1 = str(input())


    _strWord2 = str(input())

    res = levenshteinDistance(_strWord1, _strWord2);
    f.write(str(res) + "\n")

    f.close()

