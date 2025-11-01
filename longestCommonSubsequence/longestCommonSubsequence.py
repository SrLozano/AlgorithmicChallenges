class Solution:
    # time complexity: O(m*n) we need to iterate all the memo matrix
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We build a 2D DP table where:
        # dp[i][j] = length of LCS between text1[i:] and text2[j:]
        #
        # Extra row and column (+1 each) handle the "empty substring" base case
        # → This avoids out-of-bounds checks when looking at dp[i+1][j+1].
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # Iterate backwards because our dp state depends on dp[i+1][*] (future rows)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # Case 1: Characters match → take diagonal + 1
                # Meaning: we include this matching pair and move both pointers forward
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # Case 2: Characters differ → skip one character from either string
                    # Meaning: we try both possibilities and take the longer LCS
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # dp[0][0] holds the LCS length between the full strings text1 and text2
        return dp[0][0]
