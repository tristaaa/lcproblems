class Solution:
    def numRollsToTarget(self, d, f, target):

        # method 1, dfs with memonization[308 ms]
        # if d*f<target or d>target:
        #     return 0
        # if d*f==target or d==target:
        #     return 1
        # # if target is even smaller than f, 
        # # then each possible ways won't have numbers bigger than target, so the f can be set to the value of target
        # if f>target:
        #     f=target
            
        # memo={}
        # def dfs(d,target):
        #     if target<=0 or d==0:return 0
        #     if d==1:
        #         if f<target:return 0
        #         else:return 1
        #     if (d,target) in memo: return memo[(d,target)]
        #     ways=0
        #     for i in range(1,f+1):
        #         if target-i>0:
        #             ways+=dfs(d-1,target-i)
        #             ways%=(10**9+7)
        #     memo[(d,target)]=ways
        #     return ways
        
        # return dfs(d,target)



        # method 2, dp
        # if (d > target) num(d,target) = 0
        # else if (f*d < target) num(d,target) = 0
        # else if (d == target) num(d, target) = 1
        # else if (d==1 and target<=f) num(d,target) = 1
        # else num(d,t) = sum_{from k = 1 to min(f, target-1)}[ num(d-1, target-k) ]

        if d*f<target or d>target:
            return 0
        if d*f==target or d==target:
            return 1
        if f>target:
            f=target

        # dp[i][j] means the number of dice rolls with i dices when target sum = j  
        dp = [[0] *(target+1) for i in range(d+1)]

        # if d==1 and target<=f, num(d,target)=1
        for j in range(1,min(f+1,target+1)):
            dp[1][j] = 1
        # if d==target, num(d,target)=1
        for i in range(2,d+1): 
            dp[i][i]=1

        for i in range(2,d+1):
            # if d>target, num(d,target)=0, so skip the j lower than i
            # besides, when d==target, the value is preassigned
            # and if f*d<target, num(d,target)=0
            for j in range(i+1,min(i*f,target+1)):
                for k in range(1,min(f+1,j)):
                    dp[i][j] = (dp[i][j]+dp[i-1][j-k])%(10**9+7)

        return dp[d][target]%(10**9+7)

      
sol = Solution()
inputs = [(1,6,3),(2,6,7),(2,5,10),(1,2,3),(30,30,500)]
# the number of dice rolls with d=1, f=6, which can sum up to target=3 is: 1
# the number of dice rolls with d=2, f=6, which can sum up to target=7 is: 6
# the number of dice rolls with d=2, f=5, which can sum up to target=10 is: 1
# the number of dice rolls with d=1, f=2, which can sum up to target=3 is: 0
# the number of dice rolls with d=30, f=30, which can sum up to target=500 is: 222616187
for d,f,target in inputs:
    print("the number of dice rolls with d=%d, f=%d, which can sum up to target=%d is: %d" %(d,f,target,sol.numRollsToTarget(d,f, target)))

