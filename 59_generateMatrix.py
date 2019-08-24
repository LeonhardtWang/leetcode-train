class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]
        i = j = 0
        num = 1
        while num <= n ** 2:
            res[i][j] = num
            num += 1
            while j + 1 <= n - 1 and res[i][j+1] is None:
                res[i][j+1] = num 
                j += 1
                num += 1
            while i + 1 <= n - 1 and res[i+1][j] is None:
                res[i+1][j] = num
                i += 1
                num += 1
            while j - 1 >= 0 and res[i][j-1] is None:
                res[i][j-1] = num
                j -= 1
                num += 1
            while i - 1 >= 0 and res[i-1][j] is None:
                res[i-1][j] = num
                i -= 1
                num += 1
            j += 1
        return res