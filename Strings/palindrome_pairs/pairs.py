#!/bin/python3

import os
import sys

def is_palindrome(s):
    s_list = list(s)
    start = 0
    end = len(s)-1

    while(start <= end):
        if s_list[start] != s_list[end]:
            return False
        start += 1
        end -= 1
    return True

# Put reverse of all words in a dict.
# For each word, check if any of its prefix or suffix matches another word in reverse map. 
# If it does, check if its remaining word is palindrome. Then the word and its
# prefix's partner are palindrome pairs.
# O (n*k^2): Put all words in reverse map. For each word, build its substrings, compare for prefix in reverse map.
def join_words_to_make_a_palindrome(words):
    res = []
    reverse = {}
    i = 0
    for w in words:
        rev = ''.join(w[::-1])
        reverse[rev] = i
        i += 1

    for i in range(len(words)):
        w = list(words[i])
        for j in range(len(w)):
            sub1 = ''.join(w[:j+1])
            sub2 = ''.join(w[j+1:])
            if (sub1 in reverse) and (reverse[sub1] != i):
                if sub2:
                    if is_palindrome(sub2):
                        res.append((words[i], words[reverse[sub1]]))
                else:
                    res.append((words[i], words[reverse[sub1]]))

            if (sub2 in reverse) and (reverse[sub2] != i):
                if sub1:
                    if is_palindrome(sub1):
                        res.append((words[reverse[sub2]], words[i]))
                else:
                    res.append((words[reverse[sub2]], words[i]))

    return res
    

if __name__ == '__main__':
    words_count = int(input())

    words = []

    for _ in range(words_count):
        words_item = str(raw_input())
        words.append(words_item)

    res = join_words_to_make_a_palindrome(words)
    for r in res:
        print(r)

