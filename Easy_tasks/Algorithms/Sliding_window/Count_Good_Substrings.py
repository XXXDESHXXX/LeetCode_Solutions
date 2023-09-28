class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        count = i = 0
        while i <= len(s) - k:
            sub = set(s[i:i+3])
            if len(sub) == 3:
                count += 1
            i += 1
        return count