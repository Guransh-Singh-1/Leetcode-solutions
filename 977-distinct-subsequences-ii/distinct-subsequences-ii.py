class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        endswith = [0]*26

        for char in s:
            index = ord(char) - ord('a')
            endswith[index] = (sum(endswith) + 1) % MOD

        return sum(endswith) % MOD