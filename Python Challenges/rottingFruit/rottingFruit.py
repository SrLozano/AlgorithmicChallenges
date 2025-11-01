class Solution:
    # time complexity: O(m * n) as each cell is visited at most once
    # space complexity: O(m * n) as in the worst case, all cells are added to the queue
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # enqueue all initially rotten fruits (BFS starting points)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        # multi-source BFS — spread rotting effect minute by minute
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # infect adjacent fresh fruit and record time as +1 from current
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

        max_value = 0
        # determine if any fresh fruit remains and track max rotting time
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                max_value = max(max_value, grid[r][c])

        # subtract the initial value (2) to get elapsed minutes
        return max(0, max_value - 2)
