#!/bin/python3

import sys
import os
from collections import deque, defaultdict

# Given a sorted dictionary of an alien language. Find order of chars in that language.

# Graph containing dict of ordinal values of alphabets as keys, and array of its edges as values.
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topoSortUtil(self, i, visited, out):
        visited[i] = True
        
        # Visit all of adjacent vertices
        for v in self.graph[i]:
            if v not in visited:
                self.topoSortUtil(v, visited, out)

        out.appendleft(i)

    def topologicalSort(self):
        out = deque()
        visited = {}

        #import pdb; pdb.set_trace()
        for k in list(self.graph.keys()):
            if k not in visited:
                self.topoSortUtil(k, visited, out)

        return ''.join(out)


# Create a DAG as follows: Compare each pair of adjacent words, For first pair of mismatching char,
# Add a vertex from c1 to c2 to the graph. Then perform topological sort of graph
def find_order(words):
    if len(words) == 1:
        w_list = list(words[0])
        return w_list[0]

    graph = Graph()

    for i in range(1, len(words), 1):
        word1 = list(words[i-1])
        word2 = list(words[i])

        idx1 = 0
        idx2 = 0

        while (idx1 < len(word1) and idx2 < len(word2)):
            if word1[idx1] != word2[idx2]:
                # Add edge from char in word1 to char in word2
                graph.addEdge(word1[idx1], word2[idx2])
                break
            idx1 += 1
            idx2 += 1

    # Topological sort of graph vertices
    return graph.topologicalSort()

if __name__ == "__main__":
    words_cnt = 0
    words_cnt = int(input())
    words_i = 0
    words = []
    while words_i < words_cnt:
        try:
            words_item = str(raw_input())
        except:
            words_item = None
        words.append(words_item)
        words_i += 1


    res = find_order(words);
    print res

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
