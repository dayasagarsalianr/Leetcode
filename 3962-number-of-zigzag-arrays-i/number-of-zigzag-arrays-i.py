class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        r-=l
        MOD = 10**9 + 7
        prevRow = [1]*(r+1)

        for i in range(1,n):
            currRow = [0]*(r+1)
            prev = 0
            iterationRange = range(r+1) if i%2 else reversed(range(r+1))

            for j in iterationRange:
                currRow[j] = prev
                prev = (prev + prevRow[j])%MOD
                
            prevRow = currRow        

        return (sum(prevRow)*2)%MOD