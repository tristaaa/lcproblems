class Solution:
    def coinChangeTotal(self, coins, amount):
        """
        Write a function to compute the number of combinations of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return 0.

        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # original dp[i][j]=# of combinations to make up amount j by using first i types of coins, 2D:
        dp=[[0]*(amount+1) for i in range(len(coins)+1)]
        dp[0][0]=1
        for i in range(1,len(coins)+1):
            dp[i][0]=1
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if j>=coins[i-1]:
                    dp[i][j]+=dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]

        # in each iter over one denomination coins[j], 
        # the dp[i] means # of combinations to make up amount i by using the first j+1 types of coins
        dp=[0]*(amount+1)
        dp[0]=1 #there is one way to pay the amount 0 with 0 denomination. 
        for c in coins:
            for i in range(c,amount+1):
                if i>=c:
                    dp[i]+=dp[i-c]

        return dp[amount]


sol = Solution()
coins,amount = [1, 2, 5],5
print("given coins of different denominations: %s and a total amount of money: %d, there is %d kinds of combinations that make up that amount"%(coins,amount,sol.coinChangeTotal(coins,amount)))
