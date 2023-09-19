class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        for elements in nums:
            for element in nums:
                if elements > element:
                    count += 1
            ans.append(count)
            count = 0
        return ans