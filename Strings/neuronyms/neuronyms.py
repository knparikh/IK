#!/bin/python3
# L10n is neuronym of 'localization'.
# Print all possible neuronyms. Don't go under 2 as there is no further compression.

import os
import sys

# Start with 2 pointers, pointing to second and second-last char to be replaced in string.
# For each pos from loc_st to loc_end, count the chars between them. 
# Start replacing 2 to count number of chars, with count, and appropriate suffix.
# Add the char at loc_st to prefix, and start next iteration at loc_st+1.
def neuronyms(word):
    w_list = list(word)
    res = []
    loc_end = len(w_list)-2
    loc_st = 1
    prefix = w_list[0]

    #import pdb; pdb.set_trace()
    for i in range(loc_st, loc_end+1):
        # Count num_chars between loc_st to loc_end
        num_chars = loc_end - i + 1
        if num_chars > 1:
            # Create neuronyms with counts from 2 to num_chars for this pos
            for j in range(2, num_chars+1):
                last = ''.join(w_list[loc_st+j:])
                out = [prefix, str(j), last]
                res.append(''.join(out))
            prefix = prefix + w_list[loc_st]
        loc_st += 1

    return res


if __name__ == '__main__':
    word = raw_input()

    res = neuronyms(word)

    for r in res:
        print(r)

