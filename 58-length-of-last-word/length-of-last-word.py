class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = s.strip().split()
        return len(n[-1])