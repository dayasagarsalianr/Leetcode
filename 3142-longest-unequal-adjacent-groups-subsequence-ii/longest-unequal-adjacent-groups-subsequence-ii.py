class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = []
        for x in words: 
            dp.append([x])
        def hamming(a, b):
            n = len(a)
            count = 0
            for i in range(n):
                if a[i] != b[i]: 
                    count += 1
                if count > 1: 
                    return False
            return count == 1
        mx = 1
        res = [words[0]]
        for j in range(1, n):
            for i in range(0, j):
                if groups [i] != groups [j] and len (words[i]) == len(words[j]) and hamming(words[i],words[j]) and len (dp[j]) < len (dp[i]) + 1:
                    dp[j] = dp[i] + [words[j]] 
                    if len(dp[j]) > mx: 
                        mx = len(dp[j]) 
                        res = dp[j]
        return res