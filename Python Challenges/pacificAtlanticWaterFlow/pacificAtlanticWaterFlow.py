class Solution:
    # Time complexity: O(m * n) as each cell is visited at most twice
    # Space complexity: O(m * n) -> recursion stack and visited sets

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # Sets to record cells reachable from each ocean
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Stop if out of bounds, already visited, or height decreases (water can't flow upward)
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == rows or c == cols or
                heights[r][c] < prevHeight):
                return

            # Mark current cell as reachable
            visit.add((r, c))

            # Explore 4 directions (up, down, left, right)
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Run DFS for all cells adjacent to Pacific (top row and left column)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # Top border (Pacific)
            dfs(rows - 1, c, atl, heights[rows-1][c]) # Bottom border (Atlantic)

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # Left border (Pacific)
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # Right border (Atlantic)

        # Cells reachable by both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
