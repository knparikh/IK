#!/bin/python

import os
import sys
from collections import deque

# Given dictionary of words and 2 strings start and stop. How can you convert 
# start to stop with 1 char valid transformations i.e. all intermediate words 
# should be in the given dictionary. Need minimum number of transformations


def isAdjacent(word1, word2):
    w1 = list(word1)
    w2 = list(word2)

    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
        if count > 1:
            return False

    return True
            

# Since we need shortest path, we need to do BFS starting from 'start' till 'end'.
# To find adjacent vertices i.e. 1 char neighbors, go through dict and find 1 word
# adjacent words. Then add them to queue. Add to output when popping. If popped
# item is equal to 'stop' return
def string_transformation_int(words, start, stop):
    q = deque()
    pred = {}
    pred[start] = -1
    pred[stop] = -1
    q.append(start)
    #import pdb; pdb.set_trace()
    while q:
        curr = q.popleft()
        for w in words:
            if isAdjacent(w, curr):
                q.append(w)
                pred[w] = curr
                # also need to mark w visited, so remove from dict
                words.remove(w)

                if w == stop:
                    return pred
    return pred

def string_transformation(words, start, stop):
    words.append(stop)
    pred = string_transformation_int(words, start, stop)

    out = []
    curr = stop
    # Rebuild path
    out.append(stop)
    while (curr != start):
        curr = pred[curr]
        out.append(curr)

    out.reverse()
    return out


if __name__ == '__main__':

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)


    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    print('\n'.join(res))


if __name__ == '__main2__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)


    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    f.write('\n'.join(res))
    f.write('\n')
    f.close()

