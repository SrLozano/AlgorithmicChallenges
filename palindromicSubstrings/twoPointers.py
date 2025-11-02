class Solution:
    # time complexity: O(n^2)
    # space complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            # odd length substrings
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            # even length substrings
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res
