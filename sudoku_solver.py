def print_board(board):
    line = "+-------+-------+-------+"
    for i, row in enumerate(board):
        if i % 3 == 0:
            print(line)

        row_str = ""
        for j, num in enumerate(row):
            if j % 3 == 0:
                row_str += "| "
            row_str += ". " if num == 0 else f"{num} "
        row_str += "|"
        print(row_str)

    print(line)


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, num, pos):
    row, col = pos

    # Check row
    for c in range(9):
        if board[row][c] == num and c != col:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num and r != row:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if board[r][c] == num and (r, c) != pos:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


print("Sudoku Puzzle:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")