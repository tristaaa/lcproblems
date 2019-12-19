import collections
class Solution:
    def minWindow(self, s, t):
        """
        Given a string S and a string T, 
        find the minimum contiguous substring W of S, so that T is a subsequence of W
        if there are more than one substring W that have same minimum length, return the leftmost W
        """

        # 
        # method1 DP,complexity O(mn)
        # dp[i][j] means the start index of the substring W(W is a substr of S[:i] & T[:j] is a subseq of W), for the substring S[:i] and T[:j]
        # for string S[:i] and T[:j], 
        # if S[i-1]==T[i-1], dp[i][j]=dp[i-1][j-1]
        # if S[i-1]!=T[i-1], dp[i][j]=dp[i-1][j]
        
        # 1. if j>i, dp[i][j]=-1, since string T cannot be longer than S, so for i=0,j>0 all set to -1
        # 2. if j=0, dp[i][0]=i; since when S[i-1]==T[i-1], it will fetch the value from its top-left, 
        # so the dp[i][0] will be the same as dp[i+1][1] when S[:i+1]==T[0], 
        # and we know that for S[:i+1]="...a" and T="a", the start index of W is i
        
        # 3. if the dp[i][n]!=-1, we found a substring W of S that matches the conditions
        # so we store the length of W and finally find the minimum length of W
        # and we only update the `minLen` and `start` when there is a shorter W
        # if the length is the same as `minLen`, we didn't update, so we can get the leftmost W

        # m,n=len(s),len(t)
        # start,minLen=-1,m+1

        # # initialize the dp, set dp[i][0]=i, dp[0][1]=-1
        # dp=[[i] for i in range(m+1)]
        # dp[0].append(-1)

        # for i in range(1,m+1):
        #     # for the j>i, dp[i][j] must be -1, 
        #     # and we just need the value from the previous row in column j or j-1, 
        #     # so no need to compute when j>i and j must be <=n
        #     for j in range(1,min(n+1,i)):
        #         if s[i-1]==t[j-1]:
        #             dp[i].append(dp[i-1][j-1])
        #         else:
        #             dp[i].append(dp[i-1][j])
        #     if len(dp[i])<=n:
        #         dp[i].append(-1)

        #     # when for S[:i] and T[:n], the start index of W is not -1,
        #     # which means there is already a substring W of S that T is a subsequence of W
        #     if len(dp[i])==n+1 and dp[i][n]>-1:
        #         curLen = i - dp[i][n]
        #         if curLen<minLen:
        #             minLen = curLen
        #             start = dp[i][n]

        # return "" if start==-1 else s[start:start+minLen]

        # 
        # method2 two pointers,complexity O(mn)
        # To find a minimum length W, we must have the W[0]==T[0], 
        # otherwise, we can make the W shorter to clip the substring before the char that is equal to T[0]
        # so when s[i]!=t[j], we just move on the pointer i
        # when s[i]==t[j], we move on the pointer j tocompare the next char
        # only when the string t is fully a subsequence of s[:i+1], we find a possible W
        # then we move back the pointer i to the start of a local mininum W to skip the duplicate

        m,n=len(s),len(t)
        start,minLen=-1,m+1
        i,j=0,0 # pointer i,j, respectively point to the string s and t

        while i<m:
            if s[i]==t[j]: 
                # when s[i]==t[j], we move on the pointer j to compare the next char
                j+=1
                # only when t is fully includes in s[:i+1], now we find a possible W
                if j==n:
                    end = i+1 # record the end position(not included) of W
                    j-=1 # move back 1 step to make j points to the t[-1]
                    
                    # since the string s can havemany duplicate chars that matches the t[0]
                    # we need to skip these dup chars
                    # so we move the pointer i to the start of the W that is the shortest one and move the j to 0
                    # eg. for s="bbbbdde" and t="bde", we now have the i=6,j=2, then we need to move back the pointer i
                    # so that after this we can have s[i]=t[0](here i=3, so the dup 'b' are skipped), since j is decreased to -1 after this, we need to recover it
                    while j>=0:
                        while (s[i]!=t[j]):
                            i-=1
                        j-=1
                    j+=1
                    if end-i<minLen:
                        minLen = end-i
                        start=i
            i+=1

        return "" if start==-1 else s[start:start+minLen]




sol = Solution()
s,t="abcdebdde","bde"
print("Given the string S= %s, and T= %s" % (s,t))
print("find the minimum contiguous substring W of S, so that T is a subsequence of W, W= %s" % (sol.minWindow(s,t)))
# result: "bcde" since it has the minimum length that T is its subsequence, 
# and it's the the leftmost one compared to substring "bdde", where T is also the its subsequence
