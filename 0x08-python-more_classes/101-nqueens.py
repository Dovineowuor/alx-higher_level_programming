#!/usr/bin/python3
import sys


def main(n):
    queens = [[row - (row + 1) if queen %
               2 else row for queen in range(2)] for row in range(n)]
    print(queens)


def backtracking(queens, target):
    if target >= len(queens):
        return False

    while (True):
        queens[target] += 1
        if check(queens[queens]):
            pass


def check(queens):
    pass


if __name__ == "__main__":
    n = 0

    if len(sys.argv) != 2:
        sys.exit("Usage: nqueens N")

    if not sys.argv[1].isdigit():
        sys.exit("N must be a number")

    n = int(sys.argv[1])
    if n < 4:
        sys.exit("N must be at least 4")

    main(n)
