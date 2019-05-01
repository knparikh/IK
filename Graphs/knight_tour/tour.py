import os
import sys
from collections import deque

# Find shortest path from source cell to dest cell for a knight on chess board.
# http://www.techiedelight.com/chess-knight-problem-find-shortest-path-source-destination/
# Note that in BFS, all cells having shortest path as 1 are visited first, followed by their
# adjacent cells having shortest path as 1 + 1 = 2 and so on.. so if we reach any node in BFS,
# its shortest path = shortest path of parent + 1. So, the first occurrence of the destination 
# cell gives us the result and we can stop our search there. 
class cell(object):
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    visited = [[0 for j in range(cols)] for i in range(rows)]

    deq = deque()

    # Insert start cell into queue first and start processing
    deq.append(cell(start_row, start_col, 0))

    # Offsets for all possible next moves
    dx = [1, 1, -1, -1, 2, -2, 2, -2]
    dy = [2, -2, 2, -2, 1, 1, -1, -1]

    while(len(deq) > 0):
        curr = deq.popleft()

        # If we reached destination, return the distance of the cell
        if curr.x == end_row and curr.y == end_col:
            return curr.dist

        # Else for all possible next moves, push the cells in queue
        for i in range(len(dx)):
            m = dx[i]
            n = dy[i]
            new_x = curr.x + m
            new_y = curr.y + n
            if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                deq.append(cell(new_x, new_y, curr.dist+1))

    return -1


if __name__ == '__main__':
    rows = int(input())

    cols = int(input())

    start_row = int(input())

    start_col = int(input())

    end_row = int(input())

    end_col = int(input())

    res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)

    print res

if __name__ == '__main2__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    rows = int(input())

    cols = int(input())

    start_row = int(input())

    start_col = int(input())

    end_row = int(input())

    end_col = int(input())

    res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)

    f.write(str(res) + "\n")

    f.close()


