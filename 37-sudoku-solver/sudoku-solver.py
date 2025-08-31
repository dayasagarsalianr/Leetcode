class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(index):
            nonlocal solved
            if index == len(empty_cells):
                solved = True
                return
            # Fetch the current empty cell's position
            row_idx, col_idx = empty_cells[index]
            # Try each digit from 1 to 9
            for digit in range(9):
                # Check if placing digit+1 is valid in current position
                if (not row_used[row_idx][digit] and 
                    not col_used[col_idx][digit] and 
                    not block_used[row_idx // 3][col_idx // 3][digit]):
                    # Mark the digit as used in row, column, and 3x3 block
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
                    # Place the digit on the board
                    board[row_idx][col_idx] = str(digit + 1)
                    # Recursively solve for the next empty cell
                    backtrack(index + 1)
                    # If solution found, stop backtracking
                    if solved:
                        return
                    # Backtrack: undo the current placement
                    row_used[row_idx][digit] = False
                    col_used[col_idx][digit] = False
                    block_used[row_idx // 3][col_idx // 3][digit] = False
        # Initialize tracking arrays for used digits
        # row_used[i][d] = True if digit d+1 is used in row i
        row_used = [[False] * 9 for _ in range(9)]
        # col_used[j][d] = True if digit d+1 is used in column j
        col_used = [[False] * 9 for _ in range(9)]
        # block_used[bi][bj][d] = True if digit d+1 is used in block (bi, bj)
        block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        # List to store positions of empty cells
        empty_cells = []
        # Flag to indicate if solution is found
        solved = False
        # Initialize the board state and collect empty cells
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == '.':
                    # Record empty cell position
                    empty_cells.append((row_idx, col_idx))
                else:
                    # Mark existing digits as used
                    digit = int(board[row_idx][col_idx]) - 1
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
        # Start solving from the first empty cell
        backtrack(0)