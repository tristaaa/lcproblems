class Solution:
    def hasPath(self, maze, start, destination):
        """
        There is a ball in a maze with empty spaces and walls. 
        The ball can go through empty spaces by rolling up, down, left or right, 
        but it won't stop rolling until hitting a wall. 
        When the ball stops, it could choose the next direction.

        Given the ball's start position(List[int]), the destination(List[int]) and the maze(List[List[int]]), 
        determine whether the ball could stop at the destination.

        The maze is represented by a binary 2D array. 
        1 means the wall and 0 means the empty space. 
        You may assume that the borders of the maze are all walls. 
        The start and destination coordinates are represented by row and column indexes.

        The maze contains at least 2 empty spaces, 
        and both the width and height of the maze won't exceed 100.
        """
        from collections import deque
        visited = set((start[0],start[1]))
        queue = deque([start])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(maze), len(maze[0])
        while queue:
            i,j = queue.popleft()
            for d in dirs:
                # can go in one direction
                if  0<=i+d[0]<m and 0<=j+d[1]<n and maze[i+d[0]][j+d[1]] == 0:
                    x,y = i+d[0], j+d[1]
                    # keep rolling until hit the wall
                    while 0<=x+d[0]<m and 0<=y+d[1]<n and maze[x+d[0]][y+d[1]] == 0:
                        x, y = x+d[0], y+d[1]
                
                    if [x, y] == destination: return True
                    if (x, y) not in visited :
                        queue.append([x,y])
                    visited.add((x, y))
        return False

sol = Solution()
maze=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start=[0,4]
destination=[4,4]
print("Given the maze, 0 is empty space and 1 is wall: ")
print("["+str(maze[0]))
for i in maze[1:-1]:
    print(str(i)+",")
print(str(maze[-1])+"]")

print("there is a ball that can roll in empty space and won't stop rolling until hit the wall")
print("Is it possible for the ball to roll starting from position %s and ending at position %s?\n %s"%(start,destination,sol.hasPath(maze,start,destination)))


