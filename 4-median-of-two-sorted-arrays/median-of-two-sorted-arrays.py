class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_num = sorted(nums1 + nums2)
        n = len(final_num)

        if n % 2 == 0:
            return (final_num[n//2] + final_num[(n//2) - 1]) / 2.0
            
        return float(final_num[n//2])