class Solution:
    def coinChange(self, coins, amount):
        """
        Write a function to compute the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.

        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[0]*(amount+1)
        for i in range(1,amount+1):
            temp=amount
            for c in coins:
                if i>=c and dp[i-c]<temp:
                    temp=dp[i-c]
            dp[i]=temp+1

        return [dp[amount],-1][dp[amount]>amount]