class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        
        for i in range(0, len(s2) - len(s1) + 1):
            print(s2[i:i+len(s1)])
            substring = s2[i:i+len(s1)]
            if sorted(substring) == s1_sorted:
                return True

        return False