class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        multi = [k] * (n+2)
        pre = list(accumulate(multi))
        for j in pre:
                if j not in nums :
                    return j