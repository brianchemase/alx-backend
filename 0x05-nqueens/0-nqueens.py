#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given position without conflicts

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if N < 4:
        return []

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col == N:
            solutions.append([(i, board[i].index(1)) for i in range(N)])
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)

    return solutions

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solutions = solve_nqueens(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
