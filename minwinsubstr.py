import collections
class Solution:
    def minWindow(self, s, t):
        """
        Given a string S and a string T, 
        find the minimum window in S which will contain all the characters in T 
        in complexity O(n).
        """

        # sliding window
        if not s or not t or len(s)<len(t): return ''
        
        ret = ''
        hashmap = collections.defaultdict(int)
        for c in t:
            hashmap[c]+=1
            
        char_cnt = len(hashmap)
        minLen = len(s)+1 # initialize the min window length, it must be no larger than len(s)
        
        l=0
        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]]-=1
                if not hashmap[s[r]]:
                    char_cnt-=1
                    
            while not char_cnt:
                tempc = s[l]
                if tempc in hashmap:
                    hashmap[tempc]+=1
                    if hashmap[tempc]>0:
                        char_cnt+=1
                if r-l+1<minLen:
                    minLen = r-l+1
                    ret=s[l:r+1]
                l+=1
                
        return ret


sol = Solution()
s,t="ADOBECODEBANC","ABC"
print("The minimum window in S=%s which contains all the chars in T=%s is: %s" % (s,t,sol.minWindow(s,t)))
