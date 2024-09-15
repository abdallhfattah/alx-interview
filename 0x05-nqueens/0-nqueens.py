#!/usr/bin/python3
"""module that solves famous N Queen problem"""
import sys
from typing import List, Any


def solveQueens(n: int) -> List[List[int,int]]:
    """function to solve N queen problem"""
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    solutions = []
    board = [[0] * n for i in range(n)]

    def backtrack(r: int):
        if r == n:
            copy = [coll for row in board for coll in row if coll != 0]
            solutions.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            else:
                # updating
                board[r][c] = [r, c]
                posDiag.add(r + c)
                negDiag.add(r - c)
                col.add(c)
                # backtracking
                backtrack(r + 1)
                # clean up
                board[r][c] = 0
                posDiag.discard(r + c)
                negDiag.discard(r - c)
                col.discard(c)

    backtrack(0)

    return solutions


if __name__ == "__main__":
    # board dimensions
    try:
        dimensions = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if dimensions <= 3:
        print("N must be at least 4")
        sys.exit(1)

    for sol in solveQueens(dimensions):
        print(sol)
