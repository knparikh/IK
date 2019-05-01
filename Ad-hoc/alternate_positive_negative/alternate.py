#!/bin/python3

import os
import sys



# Given an array of positive and negative numbers, arrange them in an alternate
# fashion such that every positive number is followed by negative and vice-versa 
# maintaining the order of appearance.
# Soln with no extra space - O(n**2)
def rotate(numbers, start, end):
    tmp = numbers[end]
    for i in range(end, start, -1):
        numbers[i] = numbers[i-1]
    numbers[start] = tmp

def alternating_positives_and_negatives(numbers):
    out_of_place = -1
    n = len(numbers)
    import pdb; pdb.set_trace()
    for index in range(n):
        if out_of_place != -1:
            # Find the next appropriate number and rotate subarray from out_of_place index to current index
            if (numbers[out_of_place] < 0 and numbers[index] >= 0) or (numbers[out_of_place] >= 0 and numbers[index] < 0):
                rotate(numbers, out_of_place, index)
                # If index moved more than 2 spots past out_of_place, then out_of_place+2 entry is also out of place
                if index > out_of_place + 2:
                    out_of_place += 2
                else:
                    out_of_place = -1

        if out_of_place == -1:
            # If odd number at odd index or even number at even index
            if ((numbers[index] >= 0) and (index%2 == 0)) or (numbers[index]<0 and index%2 != 0):
                out_of_place = index

    return numbers
            

if __name__ == '__main__':

    numbers_count = int(input())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input())
        numbers.append(numbers_item)

    res = alternating_positives_and_negatives(numbers)

    print('\n'.join(map(str, res)))


if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input())
        numbers.append(numbers_item)

    res = alternating_positives_and_negatives(numbers)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

