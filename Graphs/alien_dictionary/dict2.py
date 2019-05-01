#!/bin/python3

import sys
import os
from collections import deque, defaultdict


def Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addAdge(self, v1, v2):
        self.graph[v1].append(v2)

    def topoSortUtil(self, v, visited, out):
        visited[v] = 1

        for neigh in self.graph[v]:
            if not visited[neigh]:
                topoSortUtil(neigh, visited, out)


        out.appendLeft(neigh)
        return

    def topoSort(self):
        out = deque()
        visited = {}

        for v in list(self.graph.keys()):
            if v not in visited:
                self, topoSortUtil(v, visited, out)

        return ''.join(out)


# Compare each pair of words, find first mismatch of chars, and add them to graph.
# Then perform topological sort.
def find_order(words):
    if len(words) == 1:
        w_list = list(words[0])
        return w_list[0]

    for i in range(1, len(words), 1):
        w1 = list(words[i-1])
        w2 = list(words[i])

        idx = 0
        graph = Graph()
        while (idx < len(w1)):
            if w1[idx] != w2[idx]:
                graph.addEdge([w1[idx]],w2[idx])
                break
            idx += 1

        return graph.topoSort()

if __name__ == "__main__":

    words_cnt = 0
    words_cnt = int(input())
    words_i = 0
    words = []
    while words_i < words_cnt:
        try:
            words_item = str(input())
        except:
            words_item = None
        words.append(words_item)
        words_i += 1


    res = find_order(words);
    print(res)


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    words_cnt = 0
    words_cnt = int(input())
    words_i = 0
    words = []
    while words_i < words_cnt:
        try:
            words_item = str(input())
        except:
            words_item = None
        words.append(words_item)
        words_i += 1


    res = find_order(words);
    f.write(res + "\n")


    f.close()

