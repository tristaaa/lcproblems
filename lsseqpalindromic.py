class Solution:
    def longestPalindromeSubseq(self, s):
        """
            find the length of the longest palindromic subsequence(can omit some char in `s`) in the given string s
            :type s: str
            :rtype: int
        """
        # method 1 [1284 ms]
        # Define: dp[i][j]=length of longest palindromic subsequence given the string s[i:j+1]
        # dp[i][j]= 2+ dp[i+1][j-1] if s[i]==s[j]
        # else, dp[i][j]= max(dp[i+1][j], dp[i][j-1])
        
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

        # method 2 [2552 ms]
        # using method for LCS(longest common subsequence)
        # Define dp[i][j] = length of longest common subsequence for string s[:i] and rd[:j]
        
        n = len(s)
        rs = s[::-1]
        dp = [[0]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rs[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[n][n]

        # method 3 [660 ms]
        # O(2n) space
        # notice that we just need the records from current array and previous array,
        # and the records are limited in the currnet column and the previous column
        # thus, we could reduce the space from n*n to n*2 

        # preprocessing to reduce time
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[1]*2 for i in range(n)]
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if s[i]==s[j]:
                    dp[i][j%2] = 2+dp[i+1][(j-1)%2] if i+1<j else 2
                else:
                    dp[i][j%2] = max(dp[i+1][j%2], dp[i][(j-1)%2])
                # print(dp)
        return dp[0][(n-1)%2]



        # method 4 [444 ms]
        # more efficient space, O(n) space
        # Define: dp[j]=length of longest palindromic subsequence given the string s[:j+1]
        # from method 1 we know, we only need the current array dp[i] and the previous dp[i+1]
        # Thus, we create the current array `newdp` and preserve the previous array `dp`
        # newdp[j] = 2 + dp[j-1] if s[i]==s[j]
        # else, newdp[j] = max(dp[j], newdp[j-1])

        # preprocessing to reduce time
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0]*n
        dp[n-1] = 1

        for i in range(n-2,-1,-1):
            newdp = dp[:]
            newdp[i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
        return dp[n-1]

        # # preprocessing to reduce time
        # if s == s[::-1]:
        #     return len(s)

        # n = len(s)
        # dp = [1]*n
        # for j in range(1,n):
        #     pre=dp[j]
        #     for i in range(j-1,-1,-1):
        #         temp = dp[i]
        #         if s[i]==s[j]:
        #             dp[i] = 2 + pre if i+1<j else 2
        #         else:
        #             dp[i] = max(dp[i+1], dp[i])
        #         pre = temp
        # return dp[0]

        


# test
sol=Solution()
s = "abbbcb"
print("the length of the longest palindromic subsequence of the string '%s' is: %s" % (s, sol.longestPalindromeSubseq(s)))
