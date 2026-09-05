class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suff_min = [0]*n
        suff_min[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suff_min[i] = min(suff_min[i+1],nums[i])
        
        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num,nums[i])
            min_num = suff_min[i]
            if max_num - min_num <= k:
                return i
        return -1