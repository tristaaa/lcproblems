class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        
        Find all the critical connections(bridge) in an undirected connected graph, with node is labeled 1..n.
        A bridge is an edge which, when removed, makes the graph disconnected.
        Equivalently, an edge is a bridge if and only if it is not contained in any cycle.
        Ouput all the bridges in incresing node idx, and an empty list if there are no bridges.
        """

        # Using the Tarjan's Alg. O(m+n)
        graph=[[] for i in range(n+1)]
        # build the undirected graph
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        # low: records the low link value of each vertex, 
        # low[u] is the lowest id of any node known to be reachable from u through u's DFS subtree, including u itself.
        # disc: records the discovery time(id) of each vertex, represent the id in Tarjan's Alg.
        # initialize the disc to -1 to use to mark if the node has been visited
        low,disc=[0]*(n+1),[-1]*(n+1)
        self.time=0 # global counter, used for the id of each vertex
        ret=[0]*((n*n-n)//2) # return list, there are at most (n^2-n)/2 possible bridges

        def dfs(u,parent):
            # initialize the low link value and the discovery time of the node u
            self.time+=1
            low[u]=disc[u]=self.time

            # visit all the neighbors of the node u
            for v in graph[u]:
                if v==parent: continue
                elif disc[v]==-1:
                    dfs(v,u)
                    print("aa",u,v)
                    low[u] = min(low[u],low[v])

                    # when the lowest node id of v's DFS subtree is larger than the node id of u
                    # then the edge(u,v) is a bridge, since the SCC(strongly connected components) of node v doesn't include node u
                    if low[v]>disc[u]:
                        # make sure for each critical connections (u,v), idx u is less than idx v
                        # and to make the whole return list sorted, add each edge(u,v) to the ret first sorted by its row(u) then by column(v)
                        # we know that for edge (u,v) if u<v, there may be at most (2*n-u)*(u-1)//2 possible bridges(u',v') whose u' is less than u
                        # and there are at most v-u-1 possible bridges(u,v') whose v' is less than v
                        if u<v: ret[(2*n-u)*(u-1)//2+v-u-1]=[u,v]
                        else: ret[(2*n-u)*(u-1)//2+u-v-1]=[v,u]

                # when node v is not the parent node of u in the DFS tree and has been visited
                # this occurs when edge(u,v) is a backwards edge (edges of G that don't belong to the DFS tree)
                # in the DFS tree
                else:
                    print("bb",u,v)
                    low[u]=min(low[u],disc[v])

        for i in range(1,n+1):
            if disc[i]==-1:
                # actually this will be called only once, since the inner loop will visit all nodes
                dfs(i,-1)

        return [cc for cc in ret if cc!=0]


sol = Solution()
n=5
connections=[[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
print("Given an undirected connected graph with %d vertexes, and with edges: %s, the graph is shown below" %(n,connections))
print("  1 - 2")
print(" / \\")
print("3 - 4 - 5")
print("\n the critical connections(bridges) are these edges(sorted in incresing id): ",sol.criticalConnections(n,connections))

n = 9
connections = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
print("Given an undirected connected graph with %d vertexes, and with edges: %s, the graph is shown below" %(n,connections))
print("  1     7 - 8")
print(" / \\    |   |")
print("2 - 3 - 6 - 9")
print("    |")
print("    4 - 5")
print("\n the critical connections(bridges) are these edges(sorted in incresing id): ",sol.criticalConnections(n,connections))
