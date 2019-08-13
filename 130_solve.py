class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        is_visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not is_visited[i][j] and board[i][j] == 'O':
                    is_visited[i][j] = True
                    board[i][j] = 'X'
                    fill_set = set([(i, j)])
                    queue = [(i, j)]
                    sign = [True]
                    while queue:
                        cur_i, cur_j = queue.pop()
                        self._helper(board, m, n, cur_i-1, cur_j, queue, fill_set, is_visited, sign) 
                        self._helper(board, m, n, cur_i+1, cur_j, queue, fill_set, is_visited, sign) 
                        self._helper(board, m, n, cur_i, cur_j-1, queue, fill_set, is_visited, sign) 
                        self._helper(board, m, n, cur_i, cur_j+1, queue, fill_set, is_visited, sign)
                    if not sign[0]:
                        for ii, jj in fill_set:
                            board[ii][jj] = 'O'
                             
    def _helper(self, board, m, n, i, j, queue, fill_set, is_visited, sign):
        if i < 0 or j < 0 or i > m - 1 or j > n - 1 or is_visited[i][j]:
            return
        if board[i][j] == 'O' and (i == 0 or i == m -1 or j == 0 or j == n - 1):
            sign[0] = False
        elif board[i][j] == 'O':
            fill_set.add((i, j))
            queue.insert(0, (i, j))
            board[i][j] = 'X'
        is_visited[i][j] = True
                        

test =[['O', 'X', 'X'],
       ['X', 'O', 'X'],
       ['X', 'X', 'X']]

Solution().solve(test)