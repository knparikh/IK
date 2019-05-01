#!/bin/python3

import sys
import os

# given input string and dictionary of words, segment the input string into a space separated sequence of dictionary of words.
# If you find multiple arrangements find all of them.
# https://www.programcreek.com/2014/03/leetcode-word-break-ii-java/

# For all prefixes starting from 0 to n-1, check if it is dictionary word.
# If it is, recursively check if remainin:g word can be broken in to words.
def wordBreakRecHelper(word, dict_words, start, result, out):

    if start == len(word):
        return

    for i in range(start, len(word), 1):
        prefix = ''.join(word[start:i+1])
        if prefix in dict_words:
            result.append(prefix)
            # Last char, so print result
            if i == len(word)-1:
                out.append(' '.join(result))
            else:
                wordBreakRecHelper(word, dict_words, i+1, result, out)
            result.pop()


def wordBreakRec(strWord, strDict):
    word = list(strWord)
    result = []
    out = []
    wordBreakRecHelper(word, strDict, 0, result, out)
    return out


# Recursive formuation
# f(i) = [] if i == len(strWord)
#      = for j in range(i, len(word))
#      =        prefix = strWord[i:j+1]
#      =        if prefix in dict:
#                       result += prefix
#                       if j == len(word)-1
#                               out.append(result)
#                       else
#                               f(i+1)
#def  wordBreak(strWord, strDict):
#    word = list(strWord)
#    out = [[] for i in range(len(strWord))]

#    for start in range(len(word)-1, -1, 1):
#        result = []
#        for i in range(start, len(word), 1):
#            prefix = ''.join(word[start:i+1])
#            if prefix in dict_words:
#                result.append(prefix)
#                # Last char, so print result
#                if i == len(word)-1:
#                    out[start] = result
#                else:
#                    result.extend(out[i+1])

#    return out[0]
        


if __name__ == "__main__":
        
    _strWord = str(input())


    _strDict_cnt = 0
    _strDict_cnt = int(input())
    _strDict_i=0
    _strDict = []
    while _strDict_i < _strDict_cnt:
        _strDict_item = str(input())
        _strDict.append(_strDict_item)
        _strDict_i+=1
        

    res = wordBreakRec(_strWord, _strDict);
    for res_cur in res:
        print(res_cur)


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
        

    _strWord = str(input())


    _strDict_cnt = 0
    _strDict_cnt = int(input())
    _strDict_i=0
    _strDict = []
    while _strDict_i < _strDict_cnt:
        _strDict_item = str(input())
        _strDict.append(_strDict_item)
        _strDict_i+=1
        

    res = wordBreak(_strWord, _strDict);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()


