class Solution:
    def repeatedSubstringPattern(self, s):
        """
            Given a non-empty string with only lowercase English letters, determine if 
            it can be constructed by repeating a substring several times(>1).

            :type s: str
            :rtype: boolean
        """
        # method 1 [36 ms]
        # Maximum length of a repeated substring of the given string would be half it's length
        # Eg. s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
        # You cannot have a substring >(len(s)/2), that can be repeated.
        # So (s+s) will have at least 4 of the substr if s is constructed by repeating the substr
        # Then by remove the first and the last of char of (s+s), we must have at least 2 of the substr
        # Thus we can find the original s in (s+s)[1:-1]
        return s in (s+s)[1:-1]

        # method 2 [56 ms]
        # def leftShift(s,l):
        #     # move the first l chars of string s to the end of the string
        #     return s[l:]+s[:l]

        # nextStr=s
        # for i in range(1,len(s)//2+1):
        #     if len(s)%i==0: # the length of repeating substr must be the divisor of len(s)
        #         nextStr = leftShift(s,i)
        #         if nextStr==s: return True
        # return False


# test
sol = Solution()
s = "abcabcabc"
print("string '%s' can be constructed by repeating a substring of it: %s" % (s,sol.repeatedSubstringPattern(s)))
