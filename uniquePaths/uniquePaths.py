class Solution:
    # Time complexity: O(m * n) — we visit each cell once
    # Space complexity: O(m * n) — we store an m×n DP table
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a DP grid with one extra row and column (m+1 x n+1)
        # The extra boundary prevents index-out-of-bounds when accessing dp[i+1][j] or dp[i][j+1]
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # Base case: there is exactly 1 way to reach the destination cell (bottom-right)
        dp[m-1][n-1] = 1

        # Fill the DP table starting from the bottom-right corner backwards to top-left
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                # Each cell's value = paths from the cell below + paths from the cell to the right
                # Because from (i, j) you can only move either down or right
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        # dp[0][0] now contains total unique paths from top-left to bottom-right
        return dp[0][0]
