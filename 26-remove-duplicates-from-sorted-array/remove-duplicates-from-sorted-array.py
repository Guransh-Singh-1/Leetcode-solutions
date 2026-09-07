class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        nums[:] = res
        return len(nums)