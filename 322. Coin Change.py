class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >=0:
                    dp[i] = min(dp[i], 1+dp[i-coin] )
        
        return dp[amount] if dp[amount] != amount+1 else -1
    
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp =[amount+1] * (amount+1)
    #     dp[0] = 0
    #     def dfs(a):
    #         if a in dp:
    #             return dp[a]
    #         for coin in coins:
    #             if a - coin >=0:
    #                 dp[a] = min(dp[a], 1+ dfs(a-coin))
    #         return dp[a]
        
    #     dfs(amount)

    #     return dp[amount] if dp[amount] != amount+1 else -1

