class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.
        """
        # go from the top-right and search like in a BST, 
        # since the left child(same row, col-1) of the root is smaller than it and 
        # the right child(same col, row+1) of the root is larger than it
        # O(m+n) since every time it rule out one row or column
        if not matrix or len(matrix)==0 or len(matrix[0])==0: return False
        
        m,n=len(matrix),len(matrix[0])
        i,j=0,n-1
        while i<m and j>-1:
            if matrix[i][j]==target: return True
            # when the current value is larger than the target, the target can only be in its left child, so go to its prev column
            elif matrix[i][j]>target: j-=1 
            else:i+=1
        return False


sol = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

print("Given the matrix: %s and the target value: %d, find out that whether the target value is in the matrix effciently: %s" % (matrix,target,sol.searchMatrix(matrix,target)))
