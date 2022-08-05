class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    row_r = self._helper(row[i], cur)
                    col_r = self._helper(col[j], cur)
                    box_r = self._helper(box[(i//3)*3+j//3], cur)
                    if not (row_r and col_r and box_r):
                        return False
        return True
                             
    def _helper(self, dic, key):
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
        if dic[key] == 2:
            return False
        else:
            return True

test = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(test))