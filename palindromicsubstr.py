class Solution:
    def countSubstrings(self, s):
        """
            Count how many palindromic substrings in the given string. 
            Substrings with different start idx or end idx are counted 
            as different substrings even they consist of same characters.

            :type s: str
            :rtype: int
        """
        # method 1 [220 ms]
        # Define: dp[i][j] denotes whether the substring s[j:i+1] is a palindrome
        # dp[i][j]= 1 if s[i]==s[j] and (j-i<2 or dp[i+1][j-1])
        # subcnt = 0
        # n = len(s)
        # dp = [[0]*n for i in range(n)]
        # for i in range(n):
        #     for j in range(i+1):
        #         if s[i]==s[j] and (i-j<2 or dp[j+1][i-1]):
        #             dp[j][i]=1
        #             subcnt+=1
        # return subcnt

        # method 2[108 ms]
        subcnt = 0
        n = len(s)

        def extendPan(s,l,r):
            cnt=0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        for i in range(n):
            subcnt +=extendPan(s,i,i)
            subcnt +=extendPan(s,i,i+1)
            
        return subcnt

        # method 3[108 ms]
        subcnt = 0
        n = len(s)
        for i in range(n):
            left=right=i
            while left >= 0 and right < n and s[left] == s[right]:
                subcnt += 1
                left -= 1
                right += 1
            left=right=i,i+1
            while left >= 0 and right < n and s[left] == s[right]:
                subcnt += 1
                left -= 1
                right += 1
        return subcnt

        # method 4 [48 ms]
        newstr = '#' + '#'.join(s) + '#'
        subcnt = 0
        n = len(newstr)
        # mid: denotes the middle position of the palindromic substring of which the right side is the rightmost
        # rmost: denotes the rightmost position of the palindromic substring of which the right side is the rightmost
        mid, rmost, maxMid, maxLen= 0,0,0,0
        # p[i] denotes the radius of a palindromic substring of which center is at idx i
        p=[0]*n
        for i in range(n):
            # 1) when i>=rmost,we cannot infer more info, so just set pi=1 and do latter job
            # set j=2*mid-1, so i,j is symmetric wrt mid
            # 2) if rmost-i>p[j], the palindromic string centered in j must be a substring of palindromic string centered in mid
            # and because of the symetric position of i,j, we know that p[i]==p[j]
            # 3) if rmost-i<=p[j], we only know for sure that
            # the substring with radius of rmost-i which centered in j must be a palindromic string,
            # thus p[i] must be at least rmost-i
            # In the above cases, we only know for sure that the case 2 gets the exact result of p[i]
            p[i] = 1 if rmost<=i else min(rmost-i, p[2*mid-i])

            # get the exact result of p[i] for case 1 and 3
            while i-p[i]>-1 and i+p[i]<length and newstr[i+p[i]]==newstr[i-p[i]]:
                p[i]+=1
            
            subcnt+=p[i]//2

            # update the varibles
            if i+p[i]>rmost:
                mid,rmost=i,i+p[i]
        return subcnt


# test
sol=Solution()
s="abcbd"
print("the number of palindromic substrings in the string: '%s' is: %d" % (s,sol.countSubstrings(s)))