#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at row, col
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row=0, board=None):
    """
    Solve N Queens using backtracking
    """
    if board is None:
        board = []

    if row == n:
        solution = []
        for r in range(n):
            solution.append([r, board[r]])
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
