class Solution:
    def shortestBridge(self, A):
        """
        In a given 2D binary array A, there are two islands.  
        (An island is a 4-directionally connected group of ones which are not connected to any other ones.)
        Now, we may change 0s to 1s so as to connect the two islands together to form one island.

        Return the smallest number of 0s that must be flipped.  
        (It is guaranteed that the answer is at least 1.)
        """
        from collections import deque
        def dfs(A,i,j,q):
            A[i][j]=2
            q.append((i,j))
            for d in dirs:
                x,y = i+d[0],j+d[1]
                if 0<=x<m and 0<=y<n and A[x][y]==1:
                    dfs(A,x,y,q)


        m,n = len(A),len(A[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        q = deque()
        # using dfs to find one island, and mark it as 2 (already visited)
        found=0
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    dfs(A,i,j,q)
                    found=1
                    break
            if found: break

        # print("mark one island as 2: ",A)
        step = 0
        # using bfs to expand the marked island
        while q:
            size=len(q)
            for i in range(size):
                cell=q.popleft()
                for d in dirs:
                    x,y = cell[0]+d[0],cell[1]+d[1]
                    if 0<=x<m and 0<=y<n and A[x][y]!=2:
                        # found another island
                        if A[x][y]==1: return step

                        # the neighbor is still water, A[x][y]==0
                        q.append((x,y))
                        A[x][y]=2
            step+=1

        return step



sol = Solution()
A = [[0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0]]
print("Given the map where indicates the location of two islands, 1 represents the land, 0 represents the sea")
print("an island is a 4-directionally connected group of ones which are not connected to any other ones")
print("["+str(A[0]))
for i in A[1:-1]:
    print(str(i)+",")
print(str(A[-1])+"]")
print("the shortest length of a bridge that connects the two islands is: ",sol.shortestBridge(A))
