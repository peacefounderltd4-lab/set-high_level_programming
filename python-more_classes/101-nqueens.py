#!/usr/bin/python3
"""N queens puzzle solution."""

import sys


def solve(n):
    """Find all solutions."""

    solutions = []

    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if col in cols:
                continue

            if row - col in diag1:
                continue

            if row + col in diag2:
                continue

            board.append([row, col])

            backtrack(
                row + 1,
                cols | {col},
                diag1 | {row - col},
                diag2 | {row + col},
                board
            )

            board.pop()

    backtrack(0, set(), set(), set(), [])

    return solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

for solution in solve(n):
    print(solution)
