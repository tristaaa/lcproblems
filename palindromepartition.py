class Solution:
    def partition(self, s):
        """
            Partition the given string into all possible palindrome partitioning.
            :type s: str
            :rtype: List[List[str]]
        """
        # method 1 [96 ms]
        # backtracking solution
        # recursively check all the partition to see if every substring is a palindrome
        def dfs(s,part,ret):
            if not s:
                ret.append(part)
                return
            for i in range(1,len(s)+1):
                # if the substring is a palindrome
                if s[:i]==s[i-1::-1]:
                    print(s,s[i:],part)
                    dfs(s[i:], part+[s[:i]], ret)

        ret=[]
        dfs(s,[],ret)
        return ret

        # method 2 [80 ms]
        # dp solution
        # dp[i] denotes all the possible partition such that each substring is a palindrome given the substring s[:i] 
        n = len(s)+1   
        dp = [[[]]]+ [[] for _ in range (n-1)]

        for i in range (1, n):
            for j in range (0, i):
                sji=s[j:i]
                if sji==sji[::-1]:
                    # if the substring s[j:i] is a palindrome, then for the given string s[:i],
                    # some of the result partition come from 
                    # all possible partition statisfied given the string s[:j] combine the substring s[j:i]
                    dp[i]+=[each+[s[j:i]] for each in dp[j]]

        return dp[-1]


# test
sol=Solution()
s="cbababdfe"
print("for string s: '%s', all possible partition such that each substring is a palindrome is: %s" % (s,sol.partition(s)))

