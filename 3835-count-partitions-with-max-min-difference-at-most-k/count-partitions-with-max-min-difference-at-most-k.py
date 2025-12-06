class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        sorted_window = SortedList()
        n = len(nums)
      
        # dp[i] = number of ways to partition nums[0:i]
        dp = [1] + [0] * n
      
        # prefix_sum[i] = cumulative sum of dp[0] to dp[i]
        prefix_sum = [1] + [0] * n
      
        # Left pointer for sliding window
        left = 1
      
        # Process each position as potential partition end
        for right in range(1, n + 1):
            # Add current element to sorted window
            sorted_window.add(nums[right - 1])
          
            # Shrink window while range exceeds k
            while sorted_window[-1] - sorted_window[0] > k:
                sorted_window.remove(nums[left - 1])
                left += 1
          
            # Calculate number of valid partitions ending at position 'right'
            # We can start a new partition from any position in [left-1, right-1]
            if left >= 2:
                dp[right] = (prefix_sum[right - 1] - prefix_sum[left - 2] + MOD) % MOD
            else:
                dp[right] = prefix_sum[right - 1] % MOD
          
            # Update prefix sum array
            prefix_sum[right] = (prefix_sum[right - 1] + dp[right]) % MOD
      
        return dp[n]
