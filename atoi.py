class Solution(object):
    def myAtoi(self, s):
        i = 0
        sign = 1
        result = 0
        
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1  
            else:
                sign = 1
            i += 1
            
        while i < len(s) and s[i].isdigit():
            
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and int(s[i]) > 7):
                if sign == 1:
                    return 2**31-1
                else:
                    return -2**31
            
            result = result * 10 + int(s[i])
            i += 1
            
        return sign * result
        
