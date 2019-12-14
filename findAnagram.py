import collections
class Solution:
    def findAnagrams(self, s, p):
        # find all the indicies of the anagrams of string p
        # Anagram: same letters but different order of the letters, 
        # here anagram of p can be in the same order of letters

        # Sliding window
        ret = []
        dict = collections.defaultdict(int)
        if not s or len(p)>len(s): return ret
        
        for c in p:
            dict[c]+=1
        
        # maintain a counter to check whether match the target string,
        # char may be duplicate.
        char_cnt = len(dict)
        
        l=0
        for r in range(len(s)):
            c = s[r]
            if c in dict:
                dict[c]-=1
                if not dict[c]:
                    char_cnt-=1

            while not char_cnt:
                tempc = s[l]
                if tempc in dict:
                    dict[tempc]+=1
                    if dict[tempc]>0:
                        char_cnt+=1
                if r-l+1==len(p):
                    ret.append(l)
                l+=1
        return ret
                
   
sol = Solution()
s="cbaebabacd"
p="abc"
print("Given the string s=%s and p=%s"%(s,p))
print("the indicies of p's anagrams are: %s"%(sol.findAnagrams(s,p)))     #[0,6]   
            
        
