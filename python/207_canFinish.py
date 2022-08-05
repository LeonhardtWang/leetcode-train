# 方法一：拓扑排序（Kahn算法）
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        adj_lis = [set() for i in range(numCourses)] # 邻接表（反映出度情况）
        in_degree = [0 for i in range(numCourses)] # 入度数组
        for aft, pre in prerequisites:
            adj_lis[aft].add(pre)
            in_degree[pre] += 1
    
        from collections import deque
        queue = deque() # 储存入度为0的节点
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        res_que = 0
        while queue:
            course = queue.pop()
            res_que += 1
            for pre in adj_lis[course]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    queue.appendleft(pre)
        return res_que == numCourses

# 方法二：深度优先遍历（用逆邻接表（反映入度情况），判断是否有环）
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        
        rev_adj_lis = [set() for _ in range(numCourses)] # 逆邻接表
        visted_lis = [0 for _ in range(numCourses)] # 0为未遍历过，1为遍历过，2为正在遍历
        for aft, pre in prerequisites:
            rev_adj_lis[pre].add(aft)
        for course in range(numCourses):
            if not self._dfs(course, rev_adj_lis, visted_lis):
                return False
        return True      

    def _dfs(self, curr_course, rev_adj_lis, visted_lis): # 有环则返回False
        if visted_lis[curr_course] == 1:
            return True
        if visted_lis[curr_course] == 2: # 又遍历到当前节点，表示有环
            return False
        visted_lis[curr_course] = 2
        for c in rev_adj_lis[curr_course]:
            if not self._dfs(c, rev_adj_lis, visted_lis):
                return False
        visted_lis[curr_course] = 1
        return True

            
print(Solution2().canFinish(2, [[1,0]]))