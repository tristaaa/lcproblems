class Solution:
    def reverse(self, x):
        """
            Given a 32-bit signed integer, reverse digits of an integer.

            Assume we are dealing with an environment which could only store integers 
            within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
            For the purpose of this problem, assume that your function returns 0 
            when the reversed integer overflows.

            :type x: int
            :rtype: int
        """
        neg = -1 if x<0 else 1
        rev = 0
        x=abs(x)
        while x:
            x,digit=divmod(x,10)
            rev = 10*rev + digit
        # not rev<=2**31, since if neg*rev=-2**31, then the input x must be out of range, which is not possible
        return neg*rev*(rev<2**31)
        # return neg*rev if rev<2**31 else 0


sol = Solution()
xs=[123,-123,0,120,2**31-1]
print("assume the environment is 32-bit, so the integer can only range from [-2**31, 2**31-1], else will return 0")
for x in xs:
    print("the reversed integer of input x= %d is: %d" % (x,sol.reverse(x)))