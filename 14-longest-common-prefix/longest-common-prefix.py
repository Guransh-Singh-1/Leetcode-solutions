class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = "" 
        strs = sorted(strs)

        first_el = strs[0]
        last_el = strs[-1]

        for i in range(min(len(first_el),len(last_el))):
            if(first_el[i]!=last_el[i]):
                return ans
            ans+=first_el[i]
        return ans   