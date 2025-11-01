class Solution:
    # time complexity: O(m*n) as 
    # space complexity: O(unique characters) because of the counter dict
     def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(s)):
            # update counter dinamically with new window
            counter[s[r]] = 1 + counter[s[r]]

            # window_length - max_counter = changes needed
            while (r - l + 1) - max(counter.values()) > k:
                # if the changes are not enough, we reduce the window
                counter[s[l]] -= 1
                l += 1
            # keep track of max
            result = max(result, r - l + 1)

        return result
        