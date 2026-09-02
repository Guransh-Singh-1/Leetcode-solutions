class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        s = s.lstrip()
        
        if not s:
            return 0
            
        sign = 1
        i = 0
        
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1
            
        num *= sign
        
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < -2 ** 31:
            return -2 ** 31
            
        return num