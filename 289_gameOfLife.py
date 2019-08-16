class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 设置四个标记：
        # 0表示死亡状态不变
        # 1表示存活状态不变
        # -1表示死亡状态变为存活状态
        # -2表示存活状态变为死亡状态
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.turn_to_state(board, i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == -2:
                    board[i][j] = 0
        
    def turn_to_state(self, board, i, j):
        left = max(0, j-1)
        right = min(len(board[0])-1, j+1)
        top = max(0, i-1)
        bottom = min(len(board)-1, i+1)
        count = 0
        for ii in range(top, bottom+1):
            for jj in range(left, right+1):
                if board[ii][jj] in {1, -2}:
                    count += 1
        if board[i][j] == 1:
            if count < 3 or count > 4:
                board[i][j] = -2
        if board[i][j] == 0:
            if count == 3:
                board[i][j] = -1
                
            