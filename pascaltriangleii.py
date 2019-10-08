class Solution:
    def getRow(self, rowIndex):
        """
        return the kth index row of the Pascal's triangle, where 0<=k<=33
        In Pascal's triangle, each number is the sum of the two numbers directly above it.
        optimize your algorithm to use only O(k) extra space

        :type rowIndex: int
        :rtype: List[int]
        """
        # dp, using O(k) extra space,
        # original: pti[i][j] = pti[i-1][j]+pti[i-1][j-1]
        # space optimized: pti[j] = pti[j]+pti[j-1]
        pti = [0]*(rowIndex+1)
        pti[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                print(i,j)
                pti[j] += pti[j-1]
        return pti

sol = Solution()
rowIndex = 4
print("the %dth index row of the Pascal's triangle is: %s " % (rowIndex,sol.getRow(rowIndex)))

