class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(words)
        last=groups[0]
        output=[words[0]]
        for i in range(1,n):
            if groups[i]!=last:
                last=groups[i]
                output.append(words[i])
        return output