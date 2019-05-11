class Solution:
    def fourSumCount(self, A, B, C, D):
        """ 
            find the count of unique index combination where those numbers add up to 0
            the four input lists are of same length 
            :type A,B,C,D: List[int]
            :rtype: int
        """
        # using hashtable
        sumAB = {}
        for a in A:
            for b in B:
                sumAB[a+b] = sumAB.get(a+b,0)+1
        return sum(sumAB.get(-c-d,0) for c in C for d in D)