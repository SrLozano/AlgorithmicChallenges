class Solution:
    # time complexity: O(2^(m+n)) as there are two choices each time we explore completely
    # space complexity: O(m+n) max recursion depth 
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1, 0), (0, 1)]

        def dfs(i, j):
            if not(i in range(m) and j in range(n)):
                return 0
            
            if i == (m-1) and j == (n-1):
                return 1

            paths = 0
            for dx, dy in directions:
                paths += dfs(i+dx, j+dy)

            return paths

        return dfs(0, 0)
