#!/bin/python3

import sys
import os

# Given number n find next smallest palindrome number
# Cases:
# 1. If input is palindrome ex. 12921, increment middle digit by 1 and 
#    propagate carry to left. Also keep copying new left digit to right.
# 2. If input is not palindrome, check the first non-matching digits starting
#    outward from middle. If left digit > right digit, simply mirror left to right.
#    If left digit < right digit, add 1 to middle digits and propagate carry to 
#    left, while mirroring left to right
# 3 If input contains all 9s, output is 1 followed by n-1 0s followed by 1

def are_all_9s(n_list):
    for i in n_list:
        if i != 9:
            return False
    return True

def next_palindrome(n):
    # Convert to list of digits
    n_list = [int(i) for i in str(n)]
    out = []

    if are_all_9s(n_list):
        out.append(1)
        for i in range(len(n_list)-1):
            out.append(0)
        out.append(1)
        n_list[:] = out[:]

    else:
        left_smaller = False
        mid = int(len(n_list)/2)
        i = mid - 1
        j = mid
        if len(n_list) % 2 == 1:
            j = mid + 1

        # Start from middle and compare left and right elements
        while (i >= 0 and (n_list[i] == n_list[j])):
            i -= 1
            j += 1

        # Case of incrementing and mirroring
        if i < 0 or n_list[i] < n_list[j]:
            left_smaller = True


        # First mirror left to right
        while(i >= 0):
            n_list[j] = n_list[i]
            i -= 1
            j += 1

        if left_smaller:
            carry = 1
            i = mid - 1

            if len(n_list) % 2 == 1:
                # Increment middle digit then carry forward and copy left to right
                n_list[mid] += carry
                carry = int(n_list[mid]/10)
                n_list[mid] = n_list[mid] % 10
                j = mid + 1
            else:
                j = mid

            # Propagate carry and mirror
            while (i >= 0):
                n_list[i] += carry
                carry = int(n_list[i]/10)
                n_list[i] = n_list[i]%10
                n_list[j] = n_list[i]
                j += 1
                i -= 1


    return ''.join(map(str, n_list))
        

if __name__ == "__main__":
    n = int(input())

    res = next_palindrome(n);
    print(res)


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    res = next_palindrome(n);
    f.write(str(res) + "\n")


    f.close()



