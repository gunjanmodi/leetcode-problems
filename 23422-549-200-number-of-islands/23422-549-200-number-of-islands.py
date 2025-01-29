class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rows_range, cols_range = set(range(rows)), set(range(cols))
        result = 0

        def dfs(i, j):
            if i not in rows_range or j not in cols_range or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1

        return result
