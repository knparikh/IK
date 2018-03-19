import math
#https://stackoverflow.com/questions/7153659/find-an-integer-not-among-four-billion-given-ones
# Find an integer not among 4 Billion given ones.
# Given an input file with 4 Billion integers, find the missing number. 
# Assume 1 GB of memory
# What if you have only 10MB memory

# With 1 GB memory: 
# 4 billion integers = 4 x 10^9 bits = 4 x 10^9 / 8 bytes = 0.5GB RAM needed to store them in bits.
# Maintain a bit array and set bit corresponding to each integer position to 1.
# # of integers needed in bit array = 4 * 10^9/ 32
# index of integer that num maps to = num/32
# index of bit inside the integer for num = num%32
# use mask 1 and right shift bit_index times to set the bit
# O(n), two passes, once to build the array, next to find missing number.
MAX = (4 * (10**9)) -1
def find_missing(fp):
    bit_array_len = int(math.ceil(4 * (10**9)/32))
    bit_array = [0 for i in range(bit_array_len)]
    for num in fp:
        num = int(num)
        index = num/32
        bit_index = num % 32
        bit_array[index] |= (1 << bit_index)

    # Once again scan the array and find missing number
    for num in range(MAX):
        index = num/32
        bit_index = num % 32
        mask = (1 << bit_index)
        if (bit_array[index] & mask) == 0:
            return num


# If memory available is 10MB, then perform k passes, each time only
# https://stackoverflow.com/questions/7153659/find-an-integer-not-among-four-billion-given-ones
#This can be solved in very little space using a variant of binary search.
#    Start off with the allowed range of numbers, 0 to 4294967295. (0-2^32)
#    Calculate the midpoint.
#    Loop through the file, counting how many numbers were equal, less than or higher than the midpoint value.
#    If no numbers were equal, you're done. The midpoint number is the answer.
#    Otherwise, choose the range that had the fewest numbers and repeat from step 2 with this new range. (0-2^31)
#This will require up to 32 linear scans through the file,, i.e. logn scans, but it will only use a few bytes of memory for storing the range and the counts.
#This is essentially the same as Henning's solution, except it uses two bins instead of 16k.
# If 4 numbers are missing, 4* logn scans needed. 1 st pass, scan numbers, count lesser, equal and more numbers than midpoint. If midpoint is non-zero, lesser and greater are equal, look at left and right for 2 missing numbers each. Call recursively till finding 1 number from a range.


# xor solution
def find_missing_xor(fp):
    #max = 2**31 - 1
    max = 17
    x1 = int(fp.readline())
    for n in fp:
        x1 ^= int(n)

    x2 = 1
    for i in range(2,max):
        x2 ^= i

    return x1 ^ x2

if __name__ == '__main__':
    with open('billion_input', 'r') as fp:
        print 'missing num = ', find_missing_xor(fp)


