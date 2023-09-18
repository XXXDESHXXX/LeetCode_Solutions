class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        if ch in word:
            right = word.index(ch)
        else:
            return word
        reverse_word = word[left:right + 1]
        reverse_word = reverse_word[::-1] + word[right + 1:]
        return reverse_word
