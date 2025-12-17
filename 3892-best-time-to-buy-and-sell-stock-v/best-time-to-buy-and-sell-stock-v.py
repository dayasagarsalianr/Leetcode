class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
      
        # dp[i][j][state] represents the maximum profit at day i with at most j transactions
        # state 0: no stock held
        # state 1: holding a bought stock (long position)
        # state 2: holding a sold stock (short position)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]
      
        # Initialize first day states for all transaction counts
        for transaction_count in range(1, k + 1):
            # Buying stock on day 0 costs prices[0]
            dp[0][transaction_count][1] = -prices[0]
            # Short selling on day 0 gains prices[0]
            dp[0][transaction_count][2] = prices[0]
      
        # Fill the dp table for each day
        for day in range(1, n):
            for transaction_count in range(1, k + 1):
                # State 0: No stock held
                # Can come from: staying without stock, selling bought stock, or buying back shorted stock
                dp[day][transaction_count][0] = max(
                    dp[day - 1][transaction_count][0],                    # Stay without stock
                    dp[day - 1][transaction_count][1] + prices[day],      # Sell bought stock
                    dp[day - 1][transaction_count][2] - prices[day]       # Buy back shorted stock
                )
              
                # State 1: Holding bought stock (long position)
                # Can come from: keeping bought stock or buying new stock (uses a transaction)
                dp[day][transaction_count][1] = max(
                    dp[day - 1][transaction_count][1],                              # Keep holding
                    dp[day - 1][transaction_count - 1][0] - prices[day]            # Buy stock
                )
              
                # State 2: Holding shorted stock (short position)
                # Can come from: keeping shorted stock or shorting new stock (uses a transaction)
                dp[day][transaction_count][2] = max(
                    dp[day - 1][transaction_count][2],                              # Keep short position
                    dp[day - 1][transaction_count - 1][0] + prices[day]            # Short sell stock
                )
      
        # Return maximum profit on last day with no stock held
        return dp[n - 1][k][0]