class Solution:
    def isPalindrome(self, x):
        """
            check if a number is palindrome.

            :type x: int
            :rtype: bool
        """
        # method 1 [64 ms]
        if x<0: return False
        strint = str(x)
        return strint==strint[::-1]

        # method 2[60 ms]
        # reverse the number x in two part
        if x<0: return False
        # p: save the highest digit of x
        # q: save the reversed the number of x except for its highest digit
        p,q=x,0
        while p>=10:
            q*=10
            q+=p%10
            p//=10
        return p==x%10 and q==x//10

        # method 3[84 ms]
        # compare the rightmost and the leftmost digits
        if x < 0: return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10
        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10
            ranger //= 100
        return True



