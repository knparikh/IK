#!/bin/python3

import sys
import os

# Implement a reg exp matcher supporting * and .
# . matches single character
# * mathces 0 or more of preceding char
def isMatchRec(s, p, pos1, pos2):
    if pos1 == len(s):
        return (pos2 == len(p))

    if pos2 == len(p):
        return (pos1 == len(s))

    if (pos2 < len(p)-1) and p[pos2+1] == '*':
        res1 = isMatchRec(s, p, pos1, pos2+2)   # Check zero occurence
        res2 = (s[pos1] == p[pos2])  # Check 1 occurence
        res3 = isMatchRec(s, p, pos1+1, pos2+2)
        res4 = isMatchRec(s, p, pos1+1, pos2) # Check more occurences
        return  res1 or (res2 and (res3 or res4))
    elif s[pos1] == p[pos2]:
        return isMatchRec(s, p, pos1+1, pos2+1)
    elif p[pos2] == '.':
        return isMatchRec(s, p, pos1+1, pos2+1)

    return False

def  isMatch(strText, strPattern):
    if strText == None or strPattern == None:
        return False

    text = list(strText)
    pattern = list(strPattern)
    return isMatchRec(text, pattern, 0, 0)

    
_strText = str(raw_input())

_strPattern = str(raw_input())

res = isMatch(_strText, _strPattern);
print res

