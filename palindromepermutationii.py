class Solution:
    def generatePalindromes(self, s):
        """
            return all the palindromic permutations (without duplicates) of the given string if exist.
            :type s: str
            :rtype: List[str]
        """
        def permute(s,start,mid,ret):
            if start>=len(s):
                ret.add(s+mid+s[::-1])
                # print("ddd:",ret)
            for i in range(start,len(s)):
                if s[i]==s[start] and i>start: continue
                # swap the char s[i] and s[start]
                if i>start:
                    s=s[:start]+s[i]+s[start+1:i]+s[start]+s[i+1:]
                    # print(s,i,start)
                permute(s,start+1,mid,ret)
                if i>start:
                    s=s[:start]+s[i]+s[start+1:i]+s[start]+s[i+1:]

        def permute2(s,hashmap,outs,mid,ret):
            if len(outs)>=len(s):
                ret.append(outs+mid+outs[::-1])
                return
            for k,v in hashmap.items():
                if v>0:
                    hashmap[k]-=1
                    permute2(s,hashmap,outs+k,mid,ret)
                    hashmap[k]+=1
                
        # method 1
        ret=set()
        half,mid='',''
        hashmap = dict.fromkeys(s,0)
        for c in s:
            hashmap[c]+=1

        for k,v in hashmap.items():
            if v%2!=0: mid+=k
            half+=k*(v//2)
            if len(mid)>1: return []
        # permute the left half string
        permute(half,0,mid,ret)

        return list(ret)

        # method 2
        ret=[]
        half,mid='',''
        hashmap = dict.fromkeys(s,0)
        for c in s:
            hashmap[c]+=1

        for k,v in hashmap.items():
            if v%2!=0: mid+=k
            hashmap[k]=v//2 #make the count halved
            half+=k*(v//2)
            if len(mid)>1: return []
        # permute the left half string
        permute2(half,hashmap,'',mid,ret)

        return ret

# test
sol=Solution()
s="aaaabbcbb"
print("all the palindromic permutations of string: '%s' is: %s" % (s, sol.generatePalindromes(s)))