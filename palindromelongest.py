class Solution:
    def longestPalindrome(self, s):
        """
            find the length of the longest panlindrome string that can be built 
            using the given chars from the string s.(case sensitive)

            :type s: str
            :rtype: int
        """
        # method 1[40 ms]
        # using hash table to count the occurrence of each char in string
        length,flag=0,0
        hashmap = dict.fromkeys(s,0)
        for c in s:
            hashmap[c]+=1
        for v in hashmap.values():
            if v%2!=0: flag = 1
            length+=v//2 * 2
        return length+1 if flag else length

        # method 2 [36 ms]
        # using replace() to count the occurrence of each char in string
        length,lens,flag=0,len(s),0
        while lens>0:
            char = s[0]
            s=s.replace(char,'')
            lens2 = len(s)
            length+=(lens-lens2)//2 * 2
            if (lens-lens2)%2: flag = 1
            lens=lens2
        return length+1 if flag else length

        
# test
sol=Solution()
s="abccccdd"
print("the length of the longest panlindrome string that can be built from the string: '%s' is: %d" % (s,sol.longestPalindrome(s)))