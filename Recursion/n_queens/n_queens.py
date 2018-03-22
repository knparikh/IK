# Check only to left cells, diagonal left top cells, diagonal left bottom cells and bottom cells,
# as we haven't computed right and top yet.
def is_safe(n, col, row, board):
    # Left side
    c = col-1
    while c >= 0:
        if board[row][c] == 'q':
            #print '1 is_safe ', row, col, 'False'
            return False
        c -= 1

    # Diagonal left top
    c = col-1
    r = row-1
    while (c >= 0) and (r >= 0):
        if board[r][c] == 'q':
            #print '2 is_safe ', row, col, 'False'
            return False
        c -= 1
        r -= 1

    c = col-1
    r = row+1
    while (c >= 0) and (r < n):
        # Diagonal left bottom
        if board[r][c] == 'q':
            #print '3 is_safe ', row, col, 'False'
            return False
        c -= 1
        r += 1

    # Bottom cell
    r = row+1
    c = col
    while (r < n):
        if board[r][c] == 'q':
            #print '4 is_safe ', row, col, 'False', 'found q at ', r, c
            return False
        r += 1

    #print 'is_safe ', row, col, 'True'
    return True

def place_queen(col, row, board):
    #print 'Placing q at', row, col
    board[row][col] = 'q'
    
def remove_queen(col, row, board):
    #print 'Removing q at', row, col
    board[row][col] = '-'


# Solve for each column, starting at 0.
# If column has reach n, append solution to output and return
# For current column, go through all rows.
#       For current row, if its safe to place queen, do so, recurse on solve for next colum
#       Unplace the queen and try for further combinations as well
def solve(n, col, out, curr):
    if (col >= n):
        curr_sol = [''.join(r) for r in curr]
        out.append(curr_sol)
        return

    for row_idx in range(n-1,-1, -1):
        if is_safe(n, col, row_idx, curr):
            place_queen(col, row_idx, curr)
            solve(n, col+1, out, curr)  # This may or may not work
            remove_queen(col, row_idx, curr)
    return


def find_all_arrangements(n):
    out = []
    curr = [['-' for i in range(n)] for j in range(n)]
    solve(n, 0, out, curr)
    return out

if __name__ == "__main__":
    n = int(input())

    res = find_all_arrangements(n);
    for res_x in res:
        for res_y in res_x:
            print res_y
        print '\n'

