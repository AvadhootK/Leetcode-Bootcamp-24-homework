class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign,i,num = 1,0,0
        if not s:
            return 0
                                    
        # if s[0] == '-':
        #     sign = s[0]
        #     s=s.replace('-','',1)
        # elif s[0]=='+':
        #     sign = s[0]
        #     s=s.replace('+','',1)
        # sdigits = ''
        # while i<len(s) and s[i].isdigit():
        #     sdigits += s[i] 
        # sdigits = sign*int(sdigits)
        # if sdigits<-2**31:
        #     sdigits = -2**31
        # elif sdigits>2**31-1:
        #     sdigits = 2**31-1
        # return sdigits

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            i+=1
        while i < len(s) and s[i].isdigit():
            sdigit = int(s[i])
            if num > (2**31 - 1 - sdigit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + sdigit
            i += 1
        return sign * num