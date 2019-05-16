class Solution:
    def addStrings(self, num1, num2):
        # method 1
        # ret=''
        # accum=0
        # lendiff = len(num1)-len(num2)
        # num1,num2 = '0'*(-lendiff)+num1, '0'*lendiff+num2

        # for i in range(1,len(num1)+1):
        #     accum,n = divmod(int(num1[-i])+int(num2[-i])+accum,10)
        #     ret+=str(n)
        # if accum:
        #     ret+=str(n)
        # return ret[::-1]

        # method 2
        ret=''
        accum=0
        num1,num2 = list(num1),list(num2)
        while num1 or num2 or accum:
            n1 = ord(num1.pop())-ord('0') if num1 else 0
            n2 = ord(num2.pop())-ord('0') if num2 else 0

            accum,n = divmod(n1+n2+accum,10)
            ret+=str(n)
        return ret[::-1]

# test
num1, num2 = '3245','79'
sol = Solution()
ret = sol.addStrings(num1,num2)
print('num1= "%s", num2= "%s", add result= "%s"' % (num1,num2,ret)) # "3324"
