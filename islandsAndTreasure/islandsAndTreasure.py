class Solution:
    # time complexity: O(m*n) as we go through all the matrix
    # space complexity: O(m*n) worst case, we work with all the matrix
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        # Step 1: enqueue all treasure positions
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Step 2: multi-source BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check boundaries
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
