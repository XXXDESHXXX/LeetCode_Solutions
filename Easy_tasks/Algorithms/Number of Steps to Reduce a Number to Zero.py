class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                steps += 1
                num //= 2
            else:
                steps += 2
                num -= 1
                num //= 2
            if num == 1:
                num -= 1
                steps += 1
        return steps