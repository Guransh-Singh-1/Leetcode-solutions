class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        ind_min = nums.index(min(nums))
        ind_max = nums.index(max(nums))

        i = min(ind_min,ind_max)
        j = max(ind_min,ind_max)  

        from_left = j+1
        from_right = n - i
        from_both = (i+1)+(n-j)   
        
        return min(from_left,from_right,from_both)