#!/bin/python3

import sys
import os


# Zombies connected with 1 or 0. Transitive property - so if z0 knows z1, z1 knows z2, then z0 knows z3.
# Find number of clusters of connected zombies.


# Perform DFS with visited flag. Number of times needed to do dfs will be total number of clusters.
def dfs(zombies, n, i, j, visited):

    for col in range(n):
        if zombies[i][col] == '1' and visited[i][col] == 0:   # If this zombie is connected and not visited yet,
            visited[i][col] = 1
            dfs(zombies, n, col, 0, visited)              # Go an visit all connected zombies in this zombie's row


def zombieCluster(zombies):
    if len(zombies) <= 1:
        return len(zombies)

    n = len(zombies)

    # Convert strings into lists
    zombies_list = [list(zombies[i]) for i in range(n)]
    visited = [[0 for i in range(n)] for j in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and zombies_list[i][j] == '1':
                #import pdb; pdb.set_trace()
                dfs(zombies_list, n, i, j, visited)
                count += 1

    return count


if __name__ == "__main__":

    zombies_cnt = 0
    zombies_cnt = int(input())
    zombies_i = 0
    zombies = []
    while zombies_i < zombies_cnt:
        try:
            zombies_item = str(raw_input())
        except:
            zombies_item = None
        zombies.append(zombies_item)
        zombies_i += 1

    res = zombieCluster(zombies);
    print res


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    zombies_cnt = 0
    zombies_cnt = int(input())
    zombies_i = 0
    zombies = []
    while zombies_i < zombies_cnt:
        try:
            zombies_item = str(raw_input())
        except:
            zombies_item = None
        zombies.append(zombies_item)
        zombies_i += 1

    res = zombieCluster(zombies);
    f.write(str(res) + "\n")

    f.close()

