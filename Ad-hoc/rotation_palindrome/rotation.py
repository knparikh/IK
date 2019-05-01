#!/bin/python3

import os
import sys

# Check if given string s is a rotation of palindrome

def is_palindrome(s):
    st = 0
    end = len(s)-1

    while (st <= end):
        if s[st] != s[end]:
            return 0
        st += 1
        end -= 1
    return 1

# Check if any of its rotations starting from 0 to n-2 is a palindrome
def check_if_rotated(s):
    if is_palindrome(s):
        return 1

    s_list = list(s)

    # Check if any of the rotations is a palindome
    for i in range(1, len(s)-1):
        s1 = s_list[:i]
        s2 = s_list[i:]

        if (is_palindrome(s2+s1)):
            return 1

    return 0

# XXX TODO
# Create concatenated string of size 2n, then find if palindrome of length n 
# exists in substrings starting from 0 to len(n)

if __name__ == '__main__':
    s = input()

    res = check_if_rotated(s)

    print(res)


if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    res = check_if_rotated(s)

    fptr.write(str(res) + '\n')

    fptr.close()

