class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        for i in range(k,n+1):
            ans = ""
            for j in range(i,n+1):
                l = s[j - i :j]
                if (not ans or l < ans) and l.count("1") == k:
                    ans = l
            if ans:
                return ans
        return ""