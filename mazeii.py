class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        There is a ball in a maze with empty spaces and walls. 
        The ball can go through empty spaces by rolling up, down, left or right, 
        but it won't stop rolling until hitting a wall. 
        When the ball stops, it could choose the next direction.
                        
        Given the ball's start position, the destination and the maze, 
        find the shortest distance for the ball to stop at the destination. 
        The distance is defined by the number of empty spaces traveled by the ball 
        from the start position (excluded) to the destination (included). 

        If the ball cannot stop at the destination, return -1.

        The maze contains at least 2 empty spaces, 
        and both the width and height of the maze won't exceed 100.
        """

        # bfs, modified Dijkstra
        import heapq
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(maze), len(maze[0])

        #record the shortest distance from the start to cell[i][j]
        shtdis = [[m*n]*n for i in range(m)] 
        shtdis[start[0]][start[1]]=0

        queue = [[0,start[0],start[1]]]
        while queue:
            # print(queue)
            # using the minheap to make sure every time we pop a new position to start rolling
            # the distance from the initial start point to this position is the smallest
            # this will make we find the shortest distance faster
            dis,i,j=heapq.heappop(queue)
            if [i,j]==destination: return shtdis[i][j]

            for d in dirs:
                # can go this direction
                if 0<=i+d[0]<m and 0<=j+d[1]<n and maze[i+d[0]][j+d[1]]==0:
                    newdis=0
                    x,y=i,j
                    # keep rolling until hit the wall
                    while 0<=x+d[0]<m and 0<=y+d[1]<n and maze[x+d[0]][y+d[1]]==0:
                        x,y=x+d[0],y+d[1]
                        newdis+=1

                    # find a shorter path from the initial start point to the [x,y]
                    if shtdis[x][y]>dis+newdis:
                        shtdis[x][y]=dis+newdis
                        heapq.heappush(queue,[dis+newdis,x,y])

        return -1
