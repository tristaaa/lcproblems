class Solution:
    def isPalindrome(self, s):
        """
            check palindrome, can delete one char. 
            string is non-empty and only contain letters: a-z

            :type s: str
            :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            # if the chars pointed by left and right are not the same
            # delete the s[l] or s[r] to see if the remaining string is a palindrome
            if s[l]!=s[r]:
                dell,delr=s[l+1:r+1],s[l:r]
                return dell==dell[::-1] or delr==delr[::-1]
            l,r=l+1,r-1
        return True

        


# test
sol=Solution()
s="abca"
print("the given string: '%s' is a palindrome (can delete one char): %s"%(s,sol.isPalindrome(s)))