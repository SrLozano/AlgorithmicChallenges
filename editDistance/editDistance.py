class Solution:
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] will store the minimum number of operations 
        # to make word1[i:] equal to word2[j:]
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Base case 1:
        # If word1 is empty (i == len(word1)), 
        # we need to insert all remaining characters of word2
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # Base case 2:
        # If word2 is empty (j == len(word2)), 
        # we need to delete all remaining characters of word1
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Fill the DP table bottom-up
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # If characters match, no operation needed — move diagonally
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    # If characters differ, consider three operations:
                    # 1. Delete current char in word1 → dp[i + 1][j]
                    # 2. Insert a char into word1 → dp[i][j + 1]
                    # 3. Replace current char → dp[i + 1][j + 1]
                    # Choose the operation with minimal cost and add 1
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],     # delete
                        dp[i][j + 1],     # insert
                        dp[i + 1][j + 1]  # replace
                    )

        # Final answer: minimum edits to convert word1 → word2
        return dp[0][0]
