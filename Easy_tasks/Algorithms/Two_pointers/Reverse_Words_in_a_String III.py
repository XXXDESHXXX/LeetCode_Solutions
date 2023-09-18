# First solution without two pointers algorithm:
class Solution:
    def reverseWords(self, s: str) -> str:
        s_strip = s.split()
        result = ''
        for word in s_strip:
            result += word[::-1] + ' '
        return result.rstrip(' ')
# Second solution with two pointers algorithm:

