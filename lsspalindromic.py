class Solution:
    def longestPalindrome(self, s):
        """
            find the longest palindromic substring in the given string s
            :type s: str
            :rtype: str
        """
        # method 1 [68 ms]
        # Iterate the string, for each character, 
        # try to expand left and right to get the longest palindromic substring
        length = len(s)
        if length<=1: return s

        start,maxLen,i=0,1,0
        while i<length:
            if i>=length - maxLen//2: break

            left,right=i,i
            # the middle char(s) of palindromic substring can be arbitrary number of the same char
            # this step skip check if the palindromic substring is of pattern:"abba" or "aba"
            while right<length-1 and s[right]==s[right+1]:
                right+=1
            # if there are many same chars on the left, just skip the steps of check these chars
            i=right+1
            while left>0 and right<length-1 and s[left-1]==s[right+1]:
                left-=1
                right+=1
            if right-left+1>maxLen:
                start,maxLen=left,right-left+1

        return s[start:start+maxLen]

        # method 2 [2476 ms]
        # DP, dp[i][j] represent whether the substring s[i:j+1] is a panlindromic string
        if not s or len(s.strip())<1: return ''

        length = len(s)
        dp = [[0] * length for _ in range(length)]

        ret=''
        for i in range(length-1,-1,-1):
            for j in range(i,length):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j]=1
                    if len(ret)<j-i+1:
                        ret=s[i:j+1]

        return ret

        # method 3 [84 ms]
        # Manacher's Algorithm
        # add an special char(not in inupt `s`) on the both sides of each char,
        # thus the new string must have odd number of chars
        newstr = '#' + '#'.join(s) + '#'

        length = len(newstr)
        # mid: denotes the middle position of the palindromic substring of which the right side is the rightmost
        # rmost: denotes the rightmost position of the palindromic substring of which the right side is the rightmost
        mid, rmost, maxMid, maxLen= 0,0,0,0
        # p[i] denotes the radius of a palindromic substring of which center is at idx i
        p=[0]*length
        for i in range(length):
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

            # update the varibles
            if i+p[i]>rmost:
                mid,rmost=i,i+p[i]
                if p[i] > maxLen:
                    maxMid,maxLen=i,p[i]
        start = (maxMid-maxLen+1)//2
        # for the string abba and new string #a#b#b#a#, the maxLen=5 is the radius of the longest palindromic substring of new string,
        # and we notice that the length of the the longest palindromic substring of the original string is exactly = maxLen-1
        return s[start:start+maxLen-1]


# test
sol =Solution()
s="babaddabcc"
print("the longest palindromic substring of the string '%s' is: %s" % (s, sol.longestPalindrome(s)))
