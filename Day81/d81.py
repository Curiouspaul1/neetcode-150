from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # create the rows and the columns
    ROWS, COLS = len(grid), len(grid[0])

    # create a visited set
    visit = set()

    # create a max area variable
    maxArea = 0

    # create a dfs function
    def dfs(r, c):
        # if the row is not in range or the column is not in range or the grid is 0 or the row and column are in the visited set
        if (r not in range(ROWS)
            or c not in range(COLS)
            or grid[r][c] == 0 or
                (r, c) in visit):
            # return 0
            return 0
        # add the row and column to the visited set
        visit.add((r, c))
        # return 1 + the dfs of the row + 1 and the column and the dfs of the row - 1 and the column and the dfs of the row and the column + 1 and the dfs of the row and the column - 1
        return (1 +
                dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1))
    # loop through the rows and columns
    for r in range(ROWS):
        for c in range(COLS):
            maxArea = max(maxArea, dfs(r, c))
    return maxArea
