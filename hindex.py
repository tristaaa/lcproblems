class Solution:
    def hIndex(self, citations):
        """
            Given an array of citations of a reasearcher, return his max h-index.
            A scientist has index h if 
            h of his/her N papers have at least h citations each, 
            and the other N − h papers have no more than h citations each.

            :type citations: List[int]
            :rtype: int
        """
        # the range of h can be [0,N]
        # method 1: easiest way, sort citations first
        # [48 ms]
        N=len(citations)
        if N==0:return 0

        citations.sort()
        for hidx in range(N-1,0,-1):
            if citations[N-hidx]>=hidx and citations[N-hidx-1]<=hidx:
                return hidx
        if citations[-1]==0: return 0
        if citations[0]>=N: return N


        # method 2: faster way, use extra space, hash table
        # [48 ms]
        N=len(citations)
        if N==0: return 0

        citecnt = [0]*(N+1)
        for cite in citations:
            if cite>N:
                citecnt[N]+=1
            else:
                citecnt[cite]+=1

        cnt=0
        for hidx in range(N,0,-1):
            # count the number of paper cites that are greater than hidx
            cnt+=citecnt[hidx]
            if cnt>=hidx:
                return hidx
        # if all the paper cites are 0, then return 0
        return 0

sol = Solution()
print("Def. H-index: h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each.")
for citations in [[],[0],[1],[0,0],[1,1],[3,0,1,6,5]]:
    print("the hindex of given the researcher's citations list: %s is: %d" % (citations, sol.hIndex(citations)))
