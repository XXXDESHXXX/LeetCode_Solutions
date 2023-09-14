class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for element in hours:
            if element >= target:
                count += 1
        return count