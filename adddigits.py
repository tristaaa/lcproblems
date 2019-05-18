class Solution:
    def addDigits(self, num):
        """
            Digit root problem: return the digit root of the input number
            Ex: for number 456, the digit root is 6 (4+5+6=15, 1+5=6)

            :type num: int
            :rtype: int
        """
        # for base b, in this case b=10, the digit root of an integer n:
            # dr(n)=0 if n==0
            # dr(n)=b-1 if n!=0 and n%(b-1)==0
            # dr(n)=n%(b-1) if n!=0 and n%(b-1)!=0
        # or generally, dr(n) = 1+(n-1)%(b-1)

        # For python the mod performs a little bit differently,
        # for -a % b(a>0,b>0), the result is b - (a%b)
        return 1 + (num-1) % 9 if num>0 else 0