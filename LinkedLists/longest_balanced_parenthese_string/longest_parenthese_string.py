#!/bin/python3
# Given a string with brackets (, ), find longest substring which is balanced.
import sys
import os

# Use a stack to record positions of open bracket. When ) bracket is encountered, pop last char (mostly a ''('').
# If stack is not empty, record length of current string as curr index - index before popped char, if more than max.
# If stack is empty, push current index to start counting for next substring.
def find_max_length_of_matching_parentheses(brackets):
    inp = list(brackets)
    max_len = 0
    stack = [-1]

    for i in range(len(inp)):
        if inp[i] == '(':
            stack.append(i)
        else:
            #char is ')', pop last char , mostly ( bracket
            stack.pop()
            # Record the length of this newly found balanced parenthese string if more than max
            if len(stack) > 0:
                len_str = i - stack[-1]
                max_len = max(max_len, len_str)
            else:
                # Stack is empty. Push this index to make base of next string
                stack.append(i)

    return max_len


if __name__ == "__main__":
    try:
        brackets = str(raw_input())
    except:
        brackets = None

    res = find_max_length_of_matching_parentheses(brackets);
    print(str(res) + "\n")

