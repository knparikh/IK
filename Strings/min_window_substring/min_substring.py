#!/bin/python3
# Given strings S and T, find min window in S which contains all chars of T
# ex. AYZABOBECODXBANC
# T = ABC  res = BANC
# If mutliple found, return any one. If none found, return empty string.
# Chars may be repeated in the pattern
import sys
import os


# Since chars in pattern can be repeated, use a couting map to represent t and also map to count chars in s.
# Start with st and end at start of string. Scan the string and update counts of chars in s_chars, if char present in t.
# Also update count only if s_chars contains less than or equal to char count in t. Otherwise, don't increment count,
# as these are extraneous chars. One count becomes equal to t_len, start optimizing from st. As soon as it reaches
# char for which s_chars[ch] would becomes less than required count, stop. Record current substring from st to end
# if its lesser than min.
def minWindowHelper(s, t, s_len, t_len):
    res = []
    st = 0
    end = 0
    min_length = len(s)
    count = 0
    s_chars = {}

    if s_len < t_len:
        return ''

    out = []
    #import pdb; pdb.set_trace()
    while end < len(s):
        ch = s[end]
        if ch in t:
            if ch in s_chars:
                s_chars[ch] += 1
            else:
                s_chars[ch] = 1
            if s_chars[ch] == t[ch]:
                count += 1
            if count == t_len:  # Found all chars
                #import pdb; pdb.set_trace()
                # Try to optimize further. Advance st as long as it does not encounter char present in t
                while st <= end:
                    ch = s[st]
                    if ch in t:
                        if s_chars[ch] == t[ch]:
                            break
                        s_chars[ch] -= 1
                    st += 1

                # Record length of substring, if its shorter
                length = end-st+1
                if length <= min_length:
                    min_length = length
                    out = s[st:end+1]
                    if min_length == len(t.keys()): # Min length cannot be lesser then length of t.
                        return ''.join(out)
        end += 1

    return ''.join(out)


def  MinWindow(strText, strCharacters):
    s = list(strText)
    t = {}
    for ch in strCharacters:
        if ch not in t:
            t[ch] = 1
        else:
            t[ch] += 1
    return minWindowHelper(s, t, len(s), len(t))

try:
    _strText = str(raw_input())
except:
    _strText = None


try:
    _strCharacters = str(raw_input())
except:
    _strCharacters = None

res = MinWindow(_strText, _strCharacters)
print res
