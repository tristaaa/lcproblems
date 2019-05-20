class Solution:
    def countBinarySubstrings(self, s):
        """
            Count(bag count) the valid substrings that have equal number of consecutive 1's and 0's,
            and the 1's and 0's are grouped together

            :type s: str
            :rtype: int
        """
        # [120ms]
        # First, count the length of consecutive 1's or 0's in the given string.
        # For example "0110001111" has consecutive 1's or 0's : ['0', '11', '000', '1111'],
        # thus, the corresponding length is [1,2,3,4]
        ll = list(map(len, s.replace('01','0 1').replace('10','1 0').split()))

        # Second, the valid substring will be the mininum length of the consecutive 1's and 0's
        # As for the substring "0001111", there are 3(min(3,4)=3) valid substrings: '01','0011','000111'
        return sum(min(a,b) for a,b in zip(ll,ll[1:]))


        # [152 ms]
        # the above idea can also be written as below, 
        # cur: record the current length of consecutive 1's or 0's
        # pre: record the previous length of consecutive 1's or 0's
        # cur,pre,ret=1,0,0
        # for i in range(1,len(s)):
        #     if s[i]==s[i-1]:
        #         cur+=1
        #     else:
        #         ret+=min(pre,cur)
        #         pre=cur
        #         cur=1

        # return ret+min(pre,cur)


# test
sol = Solution()
s="0110001111"
print("the number of valid substrings of string: '%s' that have equal number of consecutive 1's and 0's and all 1 or 0 are grouped together is: %d" % (s, sol.countBinarySubstrings(s)))
