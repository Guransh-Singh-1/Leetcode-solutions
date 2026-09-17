class Solution:
    def minSumOfLengths(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res, sum_target, i = n + 1, 0, 0

        dp = [n] * (n + 1)

        for j in range(n):
            sum_target += arr[j]

            while sum_target > k:
                sum_target -= arr[i]
                i += 1
            dp[j + 1] = dp[j]

            if sum_target == k:
                res = min(res, j - i + 1 + dp[i])
                dp[j + 1] = min(dp[j], j - i + 1)

        return -1 if res == n + 1 else res