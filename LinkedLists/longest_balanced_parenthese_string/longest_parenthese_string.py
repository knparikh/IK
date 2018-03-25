#!/bin/python3
# Given a string with brackets (, ), find longest substring which is balanced.
import sys
import os

def find_max_length_of_matching_parentheses(brackets):
    b = list(brackets)
    open_b = 0
    close_b = 0
    max_b = 0
    prev = None

    for ch in b:
        if ch == '(':
            if prev == ')':
                # Found 1st balance substring
                length = close_b*2
                if length > max_b:
                    max_b = length
                open_b = 0   # Reset counter
                close_b = 0
            open_b += 1
        elif ch == ')':
            if open_b > 0:
                open_b -= 1
                close_b += 1
                if open_b == 0:
                    # Found 1st balance substring
                    length = close_b*2
                    if length > max_b:
                        max_b = length
        prev = ch

    return max_b


if __name__ == "__main__":
    try:
        brackets = str(input())
    except:
        brackets = None

    res = find_max_length_of_matching_parentheses(brackets);
    print(str(res) + "\n")

