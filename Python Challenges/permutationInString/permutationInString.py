from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        
        # Edge case: s1 cannot be a permutation of any substring of s2
        if n > m:
            return False
        
        # Initialize hash maps for s1 and the current window in s2
        count_s1 = defaultdict(int)
        count_window = defaultdict(int)a
        
        # Populate the hash maps for the first window
        for i in range(n):
            count_s1[s1[i]] += 1
            count_window[s2[i]] += 1
        
        # Compare the first window
        if count_s1 == count_window:
            return True
        
        # Slide the window over s2
        for i in range(n, m):
            # Add the new character to the window
            count_window[s2[i]] += 1
            # Remove the old character from the window
            count_window[s2[i - n]] -= 1
            # If the count becomes zero, remove the key to keep the hash maps consistent
            if count_window[s2[i - n]] == 0:
                count_window.pop(s2[i - n])
            # Compare the hash maps
            if count_s1 == count_window:
                return True
        
        return False