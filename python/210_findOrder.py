# 方法一：拓扑排序
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        from collections import deque
        n = len(prerequisites)
        if n == 0:
            return [_ for _ in range(numCourses)]
        nei_dic = {_:set() for _ in range(numCourses)}
        degree_dic = {_:0 for _ in range(numCourses)}
        for dst, src in prerequisites:
            nei_dic[src].add(dst)
            degree_dic[dst] += 1
        
        queue = deque()
        for k in degree_dic:
            if degree_dic[k] == 0:
                queue.appendleft(k)
        
        res = []
        while queue:
            cur = queue.pop()
            res.append(cur)
            for dst in nei_dic[cur]:
                degree_dic[dst] -= 1
                if degree_dic[dst] == 0:
                    queue.append(dst)
        return res if len(res) == numCourses else []

# 方法二：深度优先遍历
class Solution2:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        if len(prerequisites) == 0:
            return [_ for _ in range(numCourses)]
        # 构造逆邻接表
        rev_adj = [set() for _ in range(numCourses)]
        for src, dst in prerequisites:
            rev_adj[src].add(dst)
        visited = [0 for _ in range(numCourses)] # 0表示未访问，1表示访问完毕，2表示正在访问
        res = []
        for i in range(numCourses):
            if self._dfs(i, rev_adj, visited, res):
                return []
        return res
    
    def _dfs(self, i, rev_adj, visited, res):# 返回是否有环
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        visited[i] = 2
        for dst in rev_adj[i]:
            if self._dfs(dst, rev_adj, visited, res):
                return True
        res.append(i)
        visited[i] = 1
        return False

print(Solution2().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
        
        