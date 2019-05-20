class Solution:
    def lengthOfLongestSubstring(self, s):
        """
            find the length of the longest substring w/o repeating chars
            :type s: str
            :rtype: int/str
        """
        if not s or len(s)<1: return 0
        
        # store the last location of the char in string s
        hashmap = {}
        # left pointer, keep two pointers which define the max substring 
        l=0
        maxLen=0
        maxLenStr=''
        
        # move the right pointer to scan the string, meanwhile update the hashmap
        for r in range(len(s)):
            # if the current char is already in the hashmap 
            # and the last location of this char is not to the left of the left pointer
            # we move the left pointer to the right of the last location of this char
            # since if the the last location of this char is to the left of the left pointer,
            # it won't affect the unquieness of the char in current max-length string
            if s[r] in hashmap and hashmap[s[r]]>=l:
                l=hashmap[s[r]]+1
            else:
                if r-l+1>maxLen:
                    maxLen=r-l+1
                    maxLenStr=s[l:r+1]

            hashmap[s[r]]=r
            
        # return maxLen
        return maxLenStr
                
        

# test
sol=Solution()
s="leetcodingforfun"
print("The longest substring w/o repeating characters of the string '%s' is: '%s'" % (s,sol.lengthOfLongestSubstring(s)))