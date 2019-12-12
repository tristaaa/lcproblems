class Solution(object):
  def mySortMat(self, mat):
    """
    sort the input matrix, size of n*n, and the output should be in this order
    [[9,8,6],
     [7,5,3],
     [4,2,1]]

    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """

    n = len(mat)
    arr = []
    for i in range(n):
      arr+=mat[i]
    arr.sort(reverse=True)
    # print(arr)

    result=[[0]*n for i in range(n)]
    for i in range(n):
      fn=i*(i+1)//2
      if i!=n-1:
        for j in range(i+1):
          result[j][i-j] = arr[fn+j]
          result[n-1-j][n-1-i+j] = arr[n*n-1-fn-j]
      else:
        for j in range(i//2+1):
          result[j][i-j] = arr[fn+j]
          result[n-1-j][n-1-i+j] = arr[n*n-1-fn-j]

    return result

sol=Solution()
mat=[
  [ 5, 1, 9, 11],
  [ 2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 0]
]
mat1=[
  [ 5, 1, 9],
  [ 2, 4, 8],
  [13, 3, 6]
]
print("Given the input matrix: [")
for i in range(len(mat)):
  print(mat[i])
print("]")
print("the sorted matrix is: [")
res=sol.mySortMat(mat)
for i in range(len(res)):
  print(res[i])
print("]")

print("Given the input matrix: [")
for i in range(len(mat1)):
  print(mat1[i])
print("]")
print("the sorted matrix is: [")
res=sol.mySortMat(mat1)
for i in range(len(res)):
  print(res[i])
print("]")
