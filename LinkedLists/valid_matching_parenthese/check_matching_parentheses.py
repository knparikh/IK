#!/bin/python3

# Check if given string has matching parentheses: '(', ')', '{', '}', '[', ']'
# Example: ( ( 1+2 ) * 3 ), Output: True
#
def hasMatchingParantheses(strExpression):
    hashmap = {')': '(', '}': '{', ']': '['}

    stack = []
    open_paren = {'(', '{', '['}
    close_paren = {')', '}', ']'}

    str_list = strExpression
    for ch in str_list:
        # Ignore non-paren chars
        if ch in open_paren:
            stack.append(ch)
        elif ch in close_paren:
            if len(stack):
                prev_ch = stack.pop()
                if prev_ch != hashmap[ch]:
                    return False
            else:
                # Did not find matching open paren
                return False

    if len(stack):
        return False
        
    return True

if __name__ == "__main__":
    try:
        strExpression = str(input())
    except:
        strExpression = None

    res = hasMatchingParantheses(strExpression);

    print res
