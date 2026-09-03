class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s

        res = ""
        cycle = 2 * numRows - 2
        for row in range(numRows):
            for i in range(row,len(s),cycle):
                res += s[i]
                hehe = i + cycle - 2 * row
                if row != 0 and row != numRows - 1 and hehe < len(s):
                    res += s[hehe]

        return res