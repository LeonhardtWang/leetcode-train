class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m < 1:
            return False
        n = len(board[0])
        if n < 1:
            return False
        path = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path[i][j] = True
                    res = self.existCore(board, word[1:], m, n, i, j, path)
                    if res:
                        return True
                    else:
                        path[i][j] = False
        return False
    
    def existCore(self, board, word, m, n, i, j, path):
        res = False
        if not word:
            return True
        if i - 1 >= 0 and path[i-1][j] == False  and board[i-1][j] == word[0]:
            path[i-1][j] = True
            res |= self.existCore(board, word[1:], m, n, i-1, j, path)
            if res:
                return res
            else:
                path[i-1][j] = False
        if j - 1 >= 0 and path[i][j-1] == False and board[i][j-1] == word[0]:
            path[i][j-1] = True
            res |= self.existCore(board, word[1:], m, n, i, j-1, path)
            if res:
                return res
            else:
                path[i][j-1] = False
        if i + 1 <= m - 1 and path[i+1][j] == False and board[i+1][j] == word[0]:
            path[i+1][j] = True
            res |= self.existCore(board, word[1:], m, n, i+1, j, path)
            if res:
                return res
            else:
                path[i+1][j] = False
        if j + 1 <= n - 1 and path[i][j+1] == False and board[i][j+1] == word[0]:
            path[i][j+1] = True
            res |= self.existCore(board, word[1:], m, n, i, j+1, path)
            if res:
                return res
            else:
                path[i][j+1] = False
        return res
            
            