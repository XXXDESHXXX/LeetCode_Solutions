class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if len(nums) <= k:
            return sum(nums) / k
        max_array = nums[:k]
        window_sum = sum(max_array)
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(window_sum, max_sum)
        return max_sum / k
