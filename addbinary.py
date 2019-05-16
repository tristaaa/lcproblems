class Solution:
    def addBinary(self, a, b):
        # method 1
        ret=''
        accum=0
        lendiff = len(a)-len(b)
        a,b = '0'*(-lendiff)+a, '0'*lendiff+b

        for i in range(1,len(a)+1):
            accum,bit = divmod(int(a[-i])+int(b[-i])+accum,2)
            ret=str(bit)+ret
        if accum:
            ret=str(accum)+ret
        return ret

        # method 2
        # return  bin(int(a, 2) + int(b, 2))[2:]

# test
a,b = '11','1'
sol = Solution()
ret1 = sol.addBinary(a,b)
print('a= "%s", b= "%s", add result= "%s"' % (a,b,ret1)) # "100"

a,b = '1010','1011'
ret2 = sol.addBinary(a,b)
print('a= "%s", b= "%s", add result= "%s"' % (a,b,ret2)) # "10101"