def knows(a,b):
    """return True when a knows b, else return False"""
    return adj[a][b]==1

class Solution:
    def findCelebrity(self, n):
        """
        Given a helper function knows, and n persons labeled 0 to n-1,
        find out if there is a celebrity(he knows nobody and others all know him) in the group,
        if yes, return the label; else return -1

        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(candidate, i):  
                # Note all candidates tranverse before are not celebrity candidates.
                candidate = i

        # Verify the candidate.
        # if the candidate knows someone or someone don't know the candidate, 
        # then the candidate cannot be the celebrity
        for i in range(candidate):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        # for the person labeled larger than the candidate,
        # candidate must not know them, so only need to verify if they know candidate
        for i in range(candidate+1,n):
            if not knows(i,candidate):
                return -1
        return candidate


sol=Solution()
adj = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]
print("given the following group of persons:")
def printAdj(adj):
    n=len(adj)
    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                print("person %d knows person %d" % (i,j))
            else:
                print("person %d doesn't know person %d" % (i,j))
printAdj(adj)
print("the group of n=%d persons has a celebrity labeled as: %d(-1 means no celebrity)" % (len(adj), sol.findCelebrity(len(adj))))


