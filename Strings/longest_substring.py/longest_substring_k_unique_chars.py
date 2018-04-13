#!/bin/python3
# Given a string, find the length of the longest substring with exactly 2 distinct chars
# Ex: s = "eceba"  T = 'ece' length 3
# If there are no such substrings (all repeated chars) print nothing
# If there are multiple such substrings, print any one.
# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

import sys
import os

# Expand and optimize sliding window
# Find the first window with 2 distinct chars and record its length.
# Keep advancing end, till distinct chars exceeds 2 (at each point recording length so far).
# Once dist_chars > 2, advance start, so we reduct dist_char to less than 2. This is to look for another substring.
# Once again continue advancing end..
# Repeat till end reaches end of string
def  longestSub(strText):
    inp = list(strText)

    start = 0
    end = 0
    distinct_chars = {}
    max_length = 0
    out_str = []

    #import pdb; pdb.set_trace()
    while(end < len(inp)):
        ch = inp[end]
        if ch not in distinct_chars:
            distinct_chars[ch] = 1
        else:
            distinct_chars[ch] += 1
        if len(distinct_chars.keys()) == 2:
            # Record length so far if max
            len_so_far = end - start + 1
            max_length = max(max_length, len_so_far)
            out_str = inp[start:end+1]
        elif len(distinct_chars.keys()) > 2:
            # We have a new char now apart from 2 distinct, advance start till we reduce distinct chars, to find another substring if it exists.
            while (start < end) and (len(distinct_chars.keys()) > 2):
                ch_start = inp[start]
                if ch_start in distinct_chars:
                    distinct_chars[ch_start] -= 1
                    if ch_start == 0:
                        del distinct_chars[ch_start]
                start += 1
        end += 1

    return ''.join(out_str)



_strText = str(raw_input())

res = longestSub(_strText);
print res
