#!/bin/python3

import sys
import os
from collections import deque, defaultdict

sys.setrecursionlimit(101000)

class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []


# Traverse through the graph, and go on adding each neighbor as key in reverse
# graph, and append parent to value list.
# This gives an adjacency list of reversed graph. Now go through the key nodes 
# in reversed_graph, and change neighbours to point to list of new neighbors in the map.
def build_other_graph_dict(node):
    reverse_graph = defaultdict(list)
    all_nodes_added = False

    #import pdb; pdb.set_trace()
    # Create a reverse_graph holding neighbor vertex as key and its parent as value
    while not all_nodes_added:
        for neighbor in node.neighbours:
            if neighbor not in reverse_graph:
                reverse_graph[neighbor].append(node)
                node = neighbor
            else:
                all_nodes_added = True

    # For each key in reverse_graph, set its neighbor
    for k, v in reverse_graph.items():
        k.neighbours = v

    return k


# Use double diamond example
# Use DFS, using visited array
# Use recursive dfs + visited works - reverse neighbors to current, after all neighbors are done.
def dfs(node, visited):
    visited[node] = 1

    if len(node.neighbours) == 0:
        return

    import pdb; pdb.set_trace()
    neighs = list(node.neighbours)
    for n in neighs:
        if n not in visited:
            # first reverse their neighbors
            dfs(n, visited)

    # Now change this node's neighbor to be node
    for n in neighs:
        n.neighbors = []
        n.neighbours.append(node)

    return


def build_other_graph(node):
    visited = {}
    dfs(node, visited)
    return node

reversed = {}

def helper_dfs(reversed_node):
    reversed[reversed_node.val] = reversed_node        
    n = len(reversed_node.neighbours)
    for i in range(0, n):
        if not reversed_node.neighbours[i].val in reversed:
            helper_dfs(reversed_node.neighbours[i])

def helper_get_all_addresses_in_reversed_graph(reversed_node):
    helper_dfs(reversed_node)
    return reversed

def helper(graph_nodes, graph_from, graph_to):
    
    MAX_NODES = 315
    
    original = {}
    for i in range(1, graph_nodes + 1):
        node = Node()
        node.val = i;
        original[i] = node
    edges = {}
    
    graph_edges = len(graph_from)
    for i in range(0, graph_edges):
        original[graph_from[i]].neighbours.append(original[graph_to[i]])
        edges[MAX_NODES * (graph_from[i] - 1) + graph_to[i] - 1] = True

    reversed = helper_get_all_addresses_in_reversed_graph(build_other_graph(original[1]))
    if (len(reversed) != graph_nodes):
        return "Wrong Answer!"

    for val in reversed.keys():
        node = reversed[val]
        if 1 > val or val > graph_nodes:
            return "Wrong Answer!"
        if original[val] == reversed[val]:
            return "Wrong Answer!"
        n = len(node.neighbours)
        for i in range(0, n):
            _val = node.neighbours[i].val
            temp = MAX_NODES * (_val - 1) + val - 1
            if not temp in edges:
                return "Wrong Answer!"
            del edges[temp]
    if len(edges) > 0:
        return "Wrong Answer!"
    return "Correct Answer!"

if __name__ == "__main__":

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for graph_i in range(graph_edges):
        graph_from[graph_i], graph_to[graph_i] = map(int, input().split())

    res = helper(graph_nodes, graph_from, graph_to)
    print(res)


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for graph_i in range(graph_edges):
        graph_from[graph_i], graph_to[graph_i] = map(int, input().split())

    res = helper(graph_nodes, graph_from, graph_to)
    f.write(res + "\n")


    f.close()


