class Solution:
    def isPalindrome(self, s):
        """
            check palindrome, ignore chars except for alphanumeric chars, ignore cases.

            :type s: str
            :rtype: bool
        """
        # method 1[40 ms]
        sl=s.lower()
        alphanum='abcdefghijklmnopqrstuvwxyz0123456789'
        cleansl = ''.join([i for i in sl if i in alphanum])
        return cleansl==cleansl[::-1]

        # method 2 [52 ms]
        sl=s.lower()
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not sl[l].isalnum():
                l += 1
            while l <r and not sl[r].isalnum():
                r -= 1
            if sl[l]!=sl[r]:
                return False
            l +=1; r -= 1
        return True


# test
sol=Solution()
s="A man, a plan, a canal: Panama"
print("the given string: '%s' is a palindrome (ignore cases, only consider alphanumeric chars): %s"%(s,sol.isPalindrome(s)))