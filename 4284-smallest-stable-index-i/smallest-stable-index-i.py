class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_num = max_num = nums[0]

        for i in range(n):
            min_num = min(nums[i:])
            if nums[i] > max_num :
                max_num = max(max_num,nums[i])
            if max_num - min_num <= k:
                return i
        return -1