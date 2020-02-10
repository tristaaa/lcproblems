class Solution:
    def searchMatrix(self, matrix, target):
        """
        Write an efficient algorithm that searches for a value in an m x n matrix.

        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
        This means that the matrix can be treated as an sorted array by concatenate each row one by one.
        """
        if not matrix or len(matrix)==0 or len(matrix[0])==0: return False
        m,n=len(matrix),len(matrix[0])
        # binary search the whole matrix
        # the matrix can be treated as a sorted array
        lo,hi=0,m*n-1
        while lo<hi:
            mid=(lo+hi+1)//2
            if matrix[mid//n][mid%n]>target:hi=mid-1
            else: lo=mid
        return matrix[lo//n][lo%n]==target


sol = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print("Given the matrix: %s and the target value: %d, find out if the target value is in the matrix efficiently: %s" %(matrix,target,sol.searchMatrix(matrix,target)))
