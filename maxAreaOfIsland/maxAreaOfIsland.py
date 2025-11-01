class Solution:
    # time complexity: O(m*n) as we need to iterate the full grid
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_size = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, island_size):
            grid[i][j] = 0 # mark visited

            for dx, dy in directions:
                mod_i, mod_j = i + dx, j + dy
                if mod_i in range(rows) and mod_j in range(cols):
                    if grid[mod_i][mod_j] == 1:
                        island_size = dfs(mod_i, mod_j, island_size+1)

            return island_size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_island_size = max(dfs(i, j, 1), max_island_size)
        
        return max_island_size
