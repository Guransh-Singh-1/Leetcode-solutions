class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        n = len(s)
        max_len = 1
        max_str = s[0]
        for i in range(n-1):
            for j in range(i+1,n):
                if j-i+1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j-i+1
                    max_str = s[i:j+1]
        
        return max_str