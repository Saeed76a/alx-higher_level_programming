#!/usr/bin/python3
import sys


class SolveNQueens:
    def __init__(self, n):
        # Attributes and variables
        self.n = n
        self.colSet = set()  # (c)  # Stores occupied columns
        self.posDiagSet = set()  # (r+c)  # Stores occupied positive diagonals
        self.negDiagSet = set()  # (r-c)  # Stores occupied negative diagonals
        self.board = self.create_board()  # Chessboard representation
        self.solution = []  # List to store valid solutions

    def create_board(self):
        # Creates an empty chessboard of size n x n
        return [[" "] * self.n for i in range(self.n)]

    def parse_solution(self, board):
        # Parses the chessboard to extract the positions of queens
        parsed_solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    parsed_solution.append([r, c])
                    break
        return parsed_solution

    def solve_by_backtracking(self, r):
        # Recursive function to solve the N-Queens problem using backtracking
        if r == self.n:
            parsed_solution = self.parse_solution(self.board)
            self.solution.append(parsed_solution)
            return
        for c in range(self.n):
            if c in self.colSet or (r + c) in self.posDiagSet:
                continue
            if (r - c) in self.negDiagSet:
                continue

            self.colSet.add(c)
            self.posDiagSet.add(r + c)
            self.negDiagSet.add(r - c)

            self.board[r][c] = "Q"

            self.solve_by_backtracking(r + 1)

            self.colSet.remove(c)
            self.posDiagSet.remove(r + c)
            self.negDiagSet.remove(r - c)
            self.board[r][c] = " "

    def solve(self):
        # Solves the N-Queens problem
        self.solve_by_backtracking(0)
        return self.solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    snq = SolveNQueens(int(sys.argv[1]))
    solutions = snq.solve()
    for solution in solutions:
        print(solution)
