class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        number = 0
        s = s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX")
        s = s.replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        for char in s:
            number += symbols[char]
        return number