
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        @cache
        def dp(i, j):
            if i == M - 1 and j == N - 1:
                return (grid[i][j],)

            this = grid[i][j]
            candidates = []

            if i + 1 < M:
                candidates.extend(dp(i + 1, j))
            
            if j + 1 < N:
                candidates.extend(dp(i, j + 1))

            return tuple(set(this ^ x for x in candidates))

        return min(dp(0, 0))
