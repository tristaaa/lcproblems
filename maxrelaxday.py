n=int(input())
# work=list(map(int,input().split()))
# exercise=list(map(int,input().split()))
work=[0,1, 1, 0, 0] 
exercise=[0,0, 1, 1, 0]

# dp[i][0] means min days relaxing with day i working
# dp[i][1] means min days relaxing with day i exercising
# dp[i][2] means min days relaxing with day i relaxing
dp=[[n]*3 for i in range(n+1)]
dp[0]=[0]*3
for i in range(1,n+1):
    if work[i]: # set day i to work
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])
    if exercise[i]: # set day i to exercise
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=min(dp[i-1])+1 # set day i to relax
print(min(dp[n]))

#     dp[i][0]=max(dp[i-1][1]+work[i],dp[i-1][0])
#     dp[i][1]=max(dp[i-1][0]+exercise[i],dp[i-1][1])
# print(n-max(dp[n][0],dp[n][1]))
