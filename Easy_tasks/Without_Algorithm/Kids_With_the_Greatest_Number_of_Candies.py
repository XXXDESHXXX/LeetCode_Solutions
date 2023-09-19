class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for elements in candies:
            if elements + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans