class Solution:
    def findShortestWay(self, maze, ball, hole):
    """
    There is a ball in a maze with empty spaces and walls. 
    The ball can go through empty spaces by rolling up, down, left or right, 
    but it won't stop rolling until hitting a wall. 
    When the ball stops, it could choose the next direction.

    There is also a hole in this maze. 
    The ball will drop into the hole if it rolls on to the hole.
                  
    Given the ball position, the hole position and the maze, 
    find out how the ball could drop into the hole by moving the shortest distance. 
    The distance is defined by the number of empty spaces traveled by the ball 
    from the start position (excluded) to the destination (included). 

    Output the moving directions by using 'u', 'd', 'l' and 'r'.
    Since there could be several different shortest ways, 
    you should output the lexicographically smallest way. 
    If the ball cannot reach the hole, output "impossible".

    The maze contains at least 2 empty spaces, 
    and both the width and height of the maze won't exceed 100.
    """
    import heapq
    # a priority queue first sorted by the shortest distance from the ball positon, 
    # then sorted by moving direction string in lexicographical order, 
    # then the current position of the ball(no need to sort this, but python's implementation of pq will sort it)
    queue = [(0, "", ball[0], ball[1])]
    m,n=len(maze),len(maze[0])

    # arrays used for exploring 4 directions from a point
    # [1,0] means go down one row
    dstr = ['d','r','u','l']
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    while queue:
        dist,dirstr,i,j=heapq.heappop(queue)

        # the current ball falls into the hole, 
        # since the first element in the priority queue must have the shortest distance to the start 
        # and the direction string is in the first in lexicographical order
        if [i,j]==hole: return dirstr

        # if the current position is visited,just skip
        if maze[i][j]==2: continue
        maze[i][j]=2 # mark as visited

        for d in dirs:
            x,y,nd=i,j,0
            while 0<=x+d[0]<m and 0<=y+d[1]<n and maze[i][j]==0:
                x,y=x+d[0],y+d[1]
                nd+=1
                if [x,y]==hole: break
            if maze[x][y]==0: # when the stop position is not visited
                heapq.heappush(queue,(dist+nd, dirstr+))


sol = Solution()
maze=[
[0 0 0 0 0],
[1 1 0 0 1],
[0 0 0 0 0],
[0 1 0 0 1],
[0 1 0 0 0]]
ball,hole=[4,3],[0,1]
print("Given the maze, 0 is empty space and 1 is wall: ")
print("["+str(maze[0]))
for i in maze[1:-1]:
    print(str(i)+",")
print(str(maze[-1])+"]")

print("there is a ball that can roll in empty space and won't stop rolling until hit the wall")
print("Given the start position of the ball: %s \n and the hole position that the should drop into: %s"%(ball,hole))
print("the moving directions of the ball that is shortest path to go to the hole with smallest lexicographical order is:", sol.findShortestWay(maze,ball,hole))

