class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        count = 0
        for sentence in sentences:
            list = sentence.split()
            for words in list:
                count += 1
            ans.append(count)
            count = 0
        print(ans)
        return max(ans)
