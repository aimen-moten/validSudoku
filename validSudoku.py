# Leetcode 38: Valid Sudoku

# Algorithm:
    # Create three empty hash sets, each that contains keys and a set of values (the key for a square hash set is (r//3, c//3))
    # Loop through each row and column
    # If the element is null, just continue with the loop
    # if it is not, then check:
    # is it in the current row or the current column or the current square?
    # if yes: return False
    # otherwise, add element to the hash set for the relevant row, column and square
    # return true outside of both loops 


# Code:
import collections
def isValidSudoku(board: list[list[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    sqs = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in sqs[(r//3,c//3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            sqs[(r//3,c//3)].add(board[r][c])
    return True

# To Test
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))