class Solution:
    # complexity: O(2^n). for each step we have two options (1 -2). We repeat n times
    def climbStairs(self, n: int) -> int:

        def dfs(i):
            if i <= 1:
                return 1
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)