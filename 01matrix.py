class Solution:
    def updateMatrix(self, matrix):
        """
        Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

        The distance between two adjacent cells is 1.(for each cell where the value is already 0, the distance to 0 is 0)
        """
        
        if not matrix or not matrix[0]: return matrix
        
        from collections import deque

        # using bfs, starting from each cell that is 0
        m,n = len(matrix), len(matrix[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    queue.append((i,j)) # starting from each cell that is 0
                else:
                    matrix[i][j] = m+n # if the cell is 1, set the distance to m+n, since it won't be larger than this
        
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        while queue:
            cell = queue.popleft()
            for d in dirs:
                x,y = cell[0]+d[0],cell[1]+d[1]
                # update the distance if the position of x,y is valid and 
                # the current distance is larger than 1 plus the known nearest distance of its adjacent cell
                if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[cell[0]][cell[1]]+1:
                    queue.append((x,y))
                    matrix[x][y] = matrix[cell[0]][cell[1]]+1

        return matrix


sol = Solution()
matrix=[
[0,0,0],
[0,1,0],
[1,1,1]
]
print("Given the matrix of 0 and 1:")
print("["+str(matrix[0]))
for i in matrix[1:-1]:
    print(str(i)+",")
print(str(matrix[-1])+"]")

print("\n the nearest distance to 0 of each cell is:")
sol.updateMatrix(matrix)

print("["+str(matrix[0]))
for i in matrix[1:-1]:
    print(str(i)+",")
print(str(matrix[-1])+"]")

