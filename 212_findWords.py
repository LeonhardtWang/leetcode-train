class Trie:
    # 前缀树（字典树）
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for s in word:
            if s not in node:
                node[s] = {}
            node = node[s]
        node['end'] = word

# 方法：前缀树+回溯
class Solution:
    def findWords(self, board: list, words: list) -> list:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.result = []
        for i in range(m):
            for j in range(n):
                self._dfs(i, j, m, n, visited, board, trie.root)
        return self.result
        
    def _dfs(self, i, j, m, n, visited, board, node):
        if board[i][j] not in node:
            return
        node = node[board[i][j]]
        if 'end' in node and node['end'] not in self.result:
            self.result.append(node['end'])
        visited[i][j] = True
        for i_, j_ in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if i_ < 0 or j_ < 0 or i_ > m - 1 or j_ > n - 1 or visited[i_][j_] or board[i_][j_] not in node:
                continue 
            self._dfs(i_, j_, m, n, visited, board, node)
        visited[i][j] = False

board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board, words))


