class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + (dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1))
        
        maxArea = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea