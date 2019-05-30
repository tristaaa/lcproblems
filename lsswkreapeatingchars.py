class Solution:
    def longestSubstring(self, s, k):
        """
            Find the length of the longest substring w/ 
            at least k repeating chars for each each.

            :type s: str
            :type k: int
            :rtype: int
        """
        # method 1 [64 ms]
        # divide and conquer, using two pointers, recursive version
        # divide the string into two parts using the rare chars, 
        # and find the length of the longest substring 
        def dc(s, l, r, k):
            if r-l<k: return 0
            for i in range(l,r):
                if s[l:r].count(s[i])<k:
                    j = i+1
                    # move the pointer j to the closest char that appear at least k times
                    while j<r and s[l:r].count(s[j])<k:
                        j+=1
                    return max(dc(s,l,i,k), dc(s,j,r,k))
            return r-l

        return dc(s, 0, len(s), k)


        # method 2 [32 ms]
        # using the rare chars to split the string, 
        # and recursively find the length of the longest substring 
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))

        # if no char in string `s` appears less than k times, the length is exactly the len(s)
        return len(s)

        # method 2.2 [40 ms]
        # iterative version, using stack
        stack = []
        stack.append(s)
        ret = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c)<k:
                    stack.extend([z for z in s.split(c)])
                    break
            # only if there is no break in the for loop, the `else` clause will be executed
            # this indicating that the whole string s is a satisfied substring
            else:
                ret = max(ret, len(s))

        return ret


# test
sol=Solution()
s="abbabc"
k=2
print("the length of the longest substring w/ at least k= %d repeating chars for each each, given the string s: '%s' is: %d" % (k,s,sol.longestSubstring(s,k)))