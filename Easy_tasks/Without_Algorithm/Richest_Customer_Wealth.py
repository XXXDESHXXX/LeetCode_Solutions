class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_el = 0
        ans = []
        for elements in accounts:
            for numbers in elements:
                max_el += numbers
            ans.append(max_el)
            max_el = 0
        print(ans)
        return max(ans)
