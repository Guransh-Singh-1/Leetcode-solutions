class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted([(nums[i], i) for i in range(n)])

        i = 0
        yo = [0] * n

        while i < n:
            j = i + 1
            while j < n and pairs[j][0] - pairs[j-1][0] <= limit:
                j += 1

            indices = sorted([pairs[k][1] for k in range(i,j)])

            for k in range(j-i):
                yo[indices[k]] = pairs[i + k][0]

            i = j
        return yo