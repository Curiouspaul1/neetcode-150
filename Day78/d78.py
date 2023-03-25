# Copilot Solution
from typing import List


def solveNQueens(n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    DFS([], [], [])
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


# Neetcode solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


# creating a multiplication table
def nMultiplicationTable(n):
    res = []
    curRow = [i for i in range(1, n+1)]
    for n in range(1, n+1):
        curRes = [n * i for i in curRow]
        res.append(curRes)
        curRes = []
    return res

assert nMultiplicationTable(5)== [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 14], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]


#print(nMultiplicationTable(5))
