class Solution:
    def canPermutePalindrome(self, s):
        """
            determine if a permutation of the string could form a palindrome
            :type s: str
            :rtype: bool
        """
        # if a palindrome can be formed by permutate chars from the given string,
        # then there must be at most one char that appears odd times.
        oddcnt=0
        hashmap = dict.fromkeys(s,0)
        for c in s:
            hashmap[c]+=1
        for v in hashmap.values():
            if v%2!=0:
                oddcnt+=1
        return oddcnt<2



# test
sol=Solution()
s="aabb"
print("a permutation of the given string: '%s' can form a palindrome: %s" % (s,sol.canPermutePalindrome(s)))