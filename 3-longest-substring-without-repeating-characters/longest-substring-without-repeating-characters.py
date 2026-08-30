class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hehe = []
        max_len = 0
        for i in s:
            while i in hehe:
                hehe.pop(0)

            hehe.append(i)
            max_len = max(max_len,len(hehe))

        return max_len