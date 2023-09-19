class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return s
