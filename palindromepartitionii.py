class Solution:
    def minCut(self, s):
        """
            find the minimum cut needed for palindrome partitioning of the given string.
            :type s: str
            :rtype: int
        """
        # method 1 [68 ms]
        # the minimum cut of all the partition is one 
        # that contains the longest palindromic substring
        # Define: cut[i] = min(cut[j-1] + 1)  for(j <= i), if s[j:i+1] is palindrome.
        # Define: dp[j][i] = 1 if s[j]==s[i] and (i-j<2 or dp[j+1][i-1]==1) else 0
        if len(s)<2:
            return 0
        if s==s[::-1]:
            return 0
        for i in range(1,len(s)):
            if s[:i] == s[i-1::-1] and s[i:] == s[:i-1:-1]:
                return 1

        n = len(s)   
        cut =[0]*n
        dp = [[0]*n for _ in range(n)]

        for i in range (n):
            cut[i]=i
            for j in range (i+1):
                if s[j]==s[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i]=1
                    cut[i] = 0 if j==0 else min(cut[i], cut[j-1]+1)
        return cut[-1]

        # method 2 [40 ms]
        # Define: dp[i] is the min cut for substring s[:i]
        # dp[i+r+1] = min(dp[i-r]+1) for r≤i and r≤n-i, if s[i-r]==s[i+r]
        if len(s)<2:
            return 0
        if s==s[::-1]:
            return 0
        for i in range(1,len(s)):
            if s[:i] == s[i-1::-1] and s[i:] == s[:i-1:-1]:
                return 1

        n = len(s)
        # initialize the min cut with max cut, which is len(s[:i])-1
        dp = [-1]+[i for i in range(n)]
        
        for i in range(1,n):
            #i is the center index of the radius, for dp[i+1]. all before i is guaranteed to be optimal.
            #odd radius
            r = 0
            while i-r>=0 and i+r<n and s[i-r] == s[i+r]:
                dp[i+r+1] = min(dp[i+r+1], dp[i-r]+1)
                r+=1
            
            #even radius, use i-1 and i as centers
            r = 0
            while i-r-1>=0 and i+r<n and s[i-r-1] == s[i+r]:
                dp[i+r+1] = min(dp[i+r+1], dp[i-r-1]+1)
                r+=1
        return dp[-1]


# test
sol=Solution()
s="cbababdfe"
print("for string s: '%s', the minimum cut among all palindrome partitioning is: %s" % (s,sol.minCut(s)))
