
#!/bin/python3

import os
import sys

# Given an array of numbers of size n, compute array of numbers products of size n
# such that products[i] is product of all numbers[j] where j!= i


def getProductArray(nums):
    # Write your code here.
    left_product = [0 for i in range(len(nums))]
    right_product = [0 for i in range(len(nums))]

    # Compute left product such that left_product[i] = product of nums[j] where j < i
    left_product[0] = 1
    for i in range(1, len(nums), 1):
        left_product[i] = left_product[i-1] * nums[i-1]

    # Compute right product such that right_product[i] = product of nums[j] where j > i
    right_product[len(nums)-1] = 1
    for i in range(len(nums)-2, -1, -1):
        right_product[i] = right_product[i+1] * nums[i+1]

    # Compute output for each position by multiplying left_product[i] * right_product[i]
    # Reuse left_product to store output
    for i in range(len(nums)-1):
        left_product[i] = left_product[i] * right_product[i]

    return left_product
        

if __name__ == '__main__':

    nums_size = int(input())

    nums = []
    for _ in range(nums_size):
        nums_item = int(input())
        nums.append(nums_item)

    res = getProductArray(nums)

    print("\n".join(map(str, res)))


if __name__ == '__main2__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nums_size = int(input())

    nums = []
    for _ in range(nums_size):
        nums_item = int(input())
        nums.append(nums_item)

    res = getProductArray(nums)

    f.write("\n".join(map(str, res)))

    f.write('\n')

    f.close()


