class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
        return count
