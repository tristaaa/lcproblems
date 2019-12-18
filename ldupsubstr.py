import collections
from functools import reduce

class Solution:
    def longestDupSubstring(self, S):
        """
            find the longest duplicated substring of S.

            :type S: str
            :rtype: str
        """
        # method 1 [1380 ms]
        # Rabin Karp algorithm
        # 1. how to find the length of the lonest string
        # 2. how to compare the string of the same length -> so we use binary search
        # 1: we can use binary search for answer since if a string of length n is invalid 
        # then for all k > n, there's definetly no solution. 
        # Similarly if a string of length n is valid, we don't have to check strings with length < n. 
        # 2: we are actually trying to compare a sliding window of string, using Rabin Karp algorithm
        # The algorithm basically computes the hash value of all the string 
        # and start a character by character comparison only if the two strings have the same hash value. 
        # In order to avoid collision we can use a large prime number such as 1e9 + 7, 19260817, 99999989, etc.

        low, high = 0, len(S) - 1
        best = ''

        A = [ord(c)-ord('a') for c in S]
        MOD = (1 << 61) - 1 # 2^61-1
        BASE = 26 # there are 26 letters from 'a' to 'z'
        def find_duplicate_substr_of_len_k(S, k):
            ''' see if there exist a substr of length k that have duplicate in the give string S '''
            D = pow(BASE, k, MOD) # same as pow(BASE, k) % MOD

            # cur = reduce(lambda x, y: (x * 26 + y) % MOD, A[:k])
            cur=A[0]
            for i in range(1,k):
                cur=(cur*26+A[i])%MOD

            seen = {cur}
            for i in range(k, len(S)):
                # calculate the hash value of the substring S[i-k+1:i+1], so add the result of A[i] and remove the result of A[i-k]
                # which is the same as reduce(lambda x, y: (x * 26 + y) % MOD, A[i-k+1:i+1])
                cur = (cur * 26 + A[i] - A[i - k] * D) % MOD 

                if cur in seen: 
                    return S[i-k+1:i+1]
                seen.add(cur)


        # using binary search
        while low < high:
            mid = (low + high + 1) // 2 # ceil((L + R) / 2)
            substrk = find_duplicate_substr_of_len_k(S, mid)
            if substrk: # like the condition that a[m]<=T
                best = substrk
                low = mid
            else:
                high = mid-1

        return best



        # method 2 [time limit exceeded]
        # using suffix array
        # Given a String we build its Suffix array and LCP (longest common Prefix)
        # The maximum LCP is the size of longest duplicated substring
        # Eg. S="banana", its suffixes are: ["banana","anana","nana","ana","na","a"]
        # and the corresponding starting idx are: 0,1,2,3,4,5
        # Thus the suffix array is: [5,3,1,0,4,2] (corresponding suffixes: ["a","ana","anana","banana","na","nana"])
        # then the corresponding LCP array is: [1,3,0,0,2,-] idx i store the LCP of suffix i and i+1,
        # Thus, the result will be max(LCP) = 3
        # n = len(S)
        # def buildSuffixArr(s):
        #     suffixes = []
        #     for i in range(n):
        #         nextRank = ord(s[i+1])-97 if i+1<n else -1
        #         suffix = [i,ord(s[i])-97,nextRank] #index, rank, nextRank
        #         suffixes.append(suffix)
        #     # sort the suffixes array first by rank then by nextRank, in asc order
        #     # Eg. [[5, 0, -1], [1, 0, 13], [3, 0, 13], [0, 1, 0], [2, 13, 0], [4, 13, 0]]
        #     suffixes.sort(key=lambda x: (x[1],x[2]))

        #     # inver[i] stores the index of the suffix with idx i (stored in suffix[i][0]) in the sorted suffixes array
        #     inver = [0]*n
        #     inver[suffixes[0][0]]=0

        #     # then sort suffixes array according to first 4 characters, then first 8 and so on
        #     k=4
        #     while k<2*n:
        #         # newrank would start from 0 and will increase 1 only if suffix i and i-1 have different rank and nextRank
        #         newrank,prevrank=0,suffixes[0][1]
        #         suffixes[0][1]=newrank
        #         for i in range(1,n):
        #             newrank = newrank if suffixes[i][1]==prevrank and suffixes[i][2]==suffixes[i-1][2] else newrank+1
        #             suffixes[i][1],prevrank = newrank,suffixes[i][1]
        #             inver[suffixes[i][0]]=i

        #         # after that, the new rank would be: [0,1,1,2,3,3] since 
        #         # in sorted suffixes array, the 2nd and 3rd suffixes have same [0,13] and the 5th and 6th suffixes have same [13,0]

        #         # assign newnextRank, 
        #         # if the suffix with idx i (stored in suffix[i][0]) have a next suffix with idx i+k//2
        #         # then store the newrank of the next suffix with idx i+k//2 to the newnextRank of suffix with idx i
        #         for i in range(n):
        #             nextidx = suffixes[i][0]+k//2
        #             suffixes[i][2] = suffixes[inver[nextidx]][1] if nextidx<n else -1

        #         # sort the suffixes array first by newrank then by newnextRank according to the first k chars
        #         suffixes.sort(key=lambda x: (x[1],x[2]))

        #         k*=2

        #     # return the indices of all the suffixes in the sorted array
        #     # [5,3,1,0,4,2]
        #     return list(map(lambda x:x[0],suffixes))

        # lcp=[0]*n
        # def kasaiAlg(s,suffArr):
        #     ''' using kasai Alg to construct the LCP array'''
        #     inverSuff=[0]*n # the value of the ith suffArr will be the idx of inverSuff, whose value is i
        #     for i in range(n):
        #         inverSuff[suffArr[i]]=i
        #     # inverSuff: [3,2,5,1,4,0]

        #     # initialize the length of the previous LCP
        #     k=0
        #     for i in range(n):
        #         if inverSuff[i]==n-1:
        #             # for the last suffix of length 1, it doesn't have a next suffix to compare, define its LCP as 0
        #             k=0
        #         else:
        #             j = suffArr[inverSuff[i]+1]
        #             while i+k<n and j+k<n and s[i+k]==s[j+k]:
        #                 k+=1
        #             lcp[inverSuff[i]] = k

        #             if k>0:
        #                 k-=1 # Deleting the starting character from the string
        #     return lcp

        # suffArr = buildSuffixArr(S)
        # kasaiAlg(S,suffArr)
        # # print(lcp)
        # lcp_len = max(lcp)
        # start = suffArr[lcp.index(lcp_len)] if lcp_len>0 else n
        # return S[start:start+lcp_len]


# test
sol=Solution()
# S="abacabaca"
S='aaaaaa'
# S="banana"
print("the longest duplicated substring of S: '%s' is: '%s'" % (S,sol.longestDupSubstring(S)))
# result: 'abaca'
# 'aaaaa'
# 'ana'
