class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        num_island = 0

        def dfs(r, c):
            if (r not in range(rows) or 
                c not in range(cols) or 
                grid[r][c] == '0'):
                return 

            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_island+=1

        return num_island