class Solution:
    def addToArrayForm(self, A, K):
        """
            Add up two integers, one in array-form, 
            return the summation in array-form.

            :type A: List[int], an array-form of integer
            :type K: int
            :rtype: List[int]
        """
        # method 1
        # ret=[]
        # Acp = A.copy()
        # while Acp or K:
        #     ai = Acp.pop() if Acp else 0
        #     K,num = divmod(ai+K,10)
        #     ret.append(num)
        # return ret[::-1]

        # method 2 
        ret=[]
        for i in range(1,len(A)+1):
            K,num = divmod(A[-i]+K,10)
            ret.append(num)
        ret = ret[::-1]
        if K: ret = list(map(int,str(K)))+ret
        return ret
# test
A, K = [1,5,1],3199
sol = Solution()
ret1 = sol.addToArrayForm(A,K)
print('A= %s, K= %d, add result= %s' % (A,K,ret1)) # [3, 3, 5, 0]

A, K = [9,9,9],1
sol = Solution()
ret2 = sol.addToArrayForm(A,K)
print('A= %s, K= %d, add result= %s' % (A,K,ret2)) # [1, 0, 0, 0]
