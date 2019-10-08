class Solution:
    def generate(self, numRows):
        """
        generate the first `numRows` of Pascal's Triangle
        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        :type numRows: int
        :rtype: List[List[int]]
        """

        result=[]
        for i in range(1,numRows+1):
            pti = [1]*i
            if i>=3:
                for j in range(1,len(pti)-1):
                    pti[j] = result[i-2][j-1] + result[i-2][j]
            result.append(pti)
        return result


sol = Solution()
numRows = 5
print("the first %d rows of pascal's triangle is: %s" % (numRows, sol.generate(numRows)))
 #     [1],
 #    [1,1],
 #   [1,2,1],
 #  [1,3,3,1],
 # [1,4,6,4,1]
