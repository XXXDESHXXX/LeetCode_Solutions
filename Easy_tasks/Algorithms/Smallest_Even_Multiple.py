class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0 and n % n == 0 :
            return n
        else:
            return n * 2
        