#!/bin/python3

import sys
import os

# Given input array of 32-bit numbers, count total number of 1s in their binary representation.
# Also known as hamming weight.

def bitCount(n):
    count = 0
    while n:
        count += 1
        n = n & (n-1)   # Resets least significant one each time.
    return count


# To avoid memory error, store # of bits for each integer in 0-255 range.
# Then, for each input number, evaluate by breaking it into 4 bytes.
def printCountOfBitsSet(intArr):
    max_int = 255
    bits = [0] * (max_int+1)

    for i in range(max_int+1):
        bits[i] = bitCount(i)

    count = 0
    for i in range(len(intArr)):
        num = intArr[i]
        for j in range(4):
            byte_num = num & max_int
            count += bits[byte_num]
            num = num >> 8

    return count


if __name__ == "__main__":

    intArr_cnt = 0
    intArr_cnt = int(input())
    intArr_i = 0
    intArr = []
    while intArr_i < intArr_cnt:
        intArr_item = int(input())
        intArr.append(intArr_item)
        intArr_i += 1


    res = printCountOfBitsSet(intArr);
    print(str(res) + "\n")



if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    intArr_cnt = 0
    intArr_cnt = int(input())
    intArr_i = 0
    intArr = []
    while intArr_i < intArr_cnt:
        intArr_item = int(input())
        intArr.append(intArr_item)
        intArr_i += 1


    res = printCountOfBitsSet(intArr);
    f.write(str(res) + "\n")


    f.close()

