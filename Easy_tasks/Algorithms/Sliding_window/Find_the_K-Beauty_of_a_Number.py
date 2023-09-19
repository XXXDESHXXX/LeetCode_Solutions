class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = len(str(num))
        str_num = str(num)
        count = i = 0
        while i <= n - k:
            sub_num = str_num[i:i+k]
            if int(sub_num) == 0:
                pass
            elif num % int(sub_num) == 0:
                count += 1
            i += 1
        return count
