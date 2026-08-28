class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if n == 1:
            return s if s > target else ""

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd_char = ""
        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd_char != "":
                    return ""  
                odd_char = chr(ord('a') + i)
            cnt[i] //= 2

        prefix = []

        for i in range(n // 2):
            for j in range(26):
                if cnt[j] == 0:
                    continue

                ch = chr(ord("a") + j)
                cnt[j] -= 1

                max_rest = "".join(chr(ord("a") + k) * cnt[k] for k in range(25, -1, -1))
                max_half = "".join(prefix) + ch + max_rest

                if max_half + odd_char + max_half[::-1] > target:
                    prefix.append(ch)

                    if ch > target[i]:
                        min_rest = "".join(chr(ord("a") + k) * cnt[k] for k in range(26))
                        half = "".join(prefix) + min_rest
                        return half + odd_char + half[::-1]
                    break

                cnt[j] += 1
            else:
                return ""

        half = "".join(prefix)
        return half + odd_char + half[::-1]