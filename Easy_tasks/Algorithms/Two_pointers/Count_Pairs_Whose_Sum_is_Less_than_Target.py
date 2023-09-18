# Variant without method sort()
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0
        right = 1
        count = 0
        while left < len(nums):
            cur_sum = nums[left] + nums[right]
            if cur_sum < target and left < right:
                count += 1
            if right == len(nums) - 1:
                left += 1
                right = 0
            right += 1
        return count
# Variant with sort() method
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        cnt = 0
        while left < right:
            if nums[left] + nums[right] < target:
                cnt += right - left
                left += 1
            else:
                right -= 1
        return cnt

