#!/bin/python3

import sys
import os

def dfs(grid, i, j, rows, cols, shortest_path, path, keys, visited):

    # If water return
    if grid[i][j] == '#':
        return

    # If door, and if key not found so far, return
    if ord(grid[i][j]) >= ord('A') and ord(grid[i][j]) <= ord('Z'):
        if grid[i][j].lower() not in keys:
            return

    is_key = 0
    # If key, then add it to key ring if we haven't seen it so far.
    if ord(grid[i][j]) >= ord('a') and ord(grid[i][j]) <= ord('z'):
        is_key = 1
        if grid[i][j] not in keys:
            keys[grid[i][j]] = 1
            print 'Reinit visit'
            # Reinitialize visited
            for vi in range(rows):
                for vj in range(cols):
                    visited[vi][vj] = 0
        else:
            keys[grid[i][j]] += 1

    if grid[i][j] == '+':
        print 'End:', path
        path.append([i,j])
        if not shortest_path or len(path) < len(shortest_path):
            shortest_path[:] = path[:]
        print 'shortest1: ', shortest_path
        path.pop()  # Delete last node
        print 'shortest2: ', shortest_path
        return

    visited[i][j] = 1
    path.append([i,j])
    print path

    # Explore adjacents grids
    if i+1 < rows and visited[i+1][j] == 0:
        dfs(grid, i+1, j, rows, cols, shortest_path, path, keys, visited)
    if i-1 >= 0 and visited[i-1][j] == 0:
        dfs(grid, i-1, j, rows, cols, shortest_path, path, keys, visited)
    if j+1 < cols and visited[i][j+1] == 0:
        dfs(grid, i, j+1, rows, cols, shortest_path, path, keys, visited)
    if j-1 >= 0 and visited[i][j-1] == 0:
        dfs(grid, i, j-1, rows, cols, shortest_path, path, keys, visited)

    path.pop()  # Delete last node
    visited[i][j] = 0
    if is_key:
        # Remove from key ring
        keys[grid[i][j]] -= 1
        if keys[grid[i][j]] == 0:
            del keys[grid[i][j]]

    return

def find_shortest_path(grid):
    inp_grid = [list(w) for w in grid]
    rows = len(inp_grid)
    cols = len(inp_grid[0])

    visited = [[0 for j in range(cols)] for i in range(rows)]

    shortest_path = []
    path = []
    keys = {}
    for i in range(rows):
        for j in range(cols):
            if inp_grid[i][j] == '@':
                #import pdb; pdb.set_trace()
                dfs(grid, i, j, rows, cols, shortest_path, path, keys, visited)
                break

    return shortest_path


if __name__ == "__main__":
    grid_cnt = 0
    grid_cnt = int(input())
    grid_i = 0
    grid = []
    while grid_i < grid_cnt:
        try:
            grid_item = str(raw_input())
        except:
            grid_item = None
        grid.append(grid_item)
        grid_i += 1

    res = find_shortest_path(grid);
    for res_x in res:
        for res_y in res_x:
            print res_y,
        print '\n'


if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    grid_cnt = 0
    grid_cnt = int(input())
    grid_i = 0
    grid = []
    while grid_i < grid_cnt:
        try:
            grid_item = str(input())
        except:
            grid_item = None
        grid.append(grid_item)
        grid_i += 1

    res = find_shortest_path(grid);
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")


    f.close()
