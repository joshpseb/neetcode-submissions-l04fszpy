class Solution: #iterative
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                row, col = stack.pop()
                if row >= ROWS or col >= COLS or row < 0 or col < 0:
                    continue
                if grid[row][col] == "0":
                    continue
                grid[row][col] = "0"

                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res
        
        