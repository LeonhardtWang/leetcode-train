class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        nei_dic = {}
        for i, v in enumerate(equations):
            if v[0] not in nei_dic:
                nei_dic[v[0]] = {}
                nei_dic[v[0]][v[1]] = values[i]
            else:
                nei_dic[v[0]][v[1]] = values[i]
                
            if v[1] not in nei_dic:
                nei_dic[v[1]] = {}
                nei_dic[v[1]][v[0]] = 1 / values[i]
            else:
                nei_dic[v[1]][v[0]] = 1 / values[i]
        res = []
        for b, e in queries:
            if b in nei_dic and b == e: # 注意要防止被除字符不在邻接表里
                res.append(1)
                continue
            tra_path = [b]
            is_find = self._helper(nei_dic, b, e, tra_path)
            if is_find:
                tmp = 1
                for i in range(len(tra_path)-1):
                    tmp *= nei_dic[tra_path[i]][tra_path[i+1]]
                res.append(tmp)
            else:
                res.append(-1)
        return res
        
    def _helper(self, nei_dic, begin, end, tra_path):
        if begin in nei_dic:
            next_dic = nei_dic[begin]
            for next_k in next_dic:
                if next_k not in tra_path:
                    tra_path.append(next_k)
                    if next_k == end:
                        return True
                    is_route = self._helper(nei_dic, next_k, end, tra_path)
                    if is_route:
                        return is_route
                    else:
                        tra_path.pop()
        return False
                

print(Solution().calcEquation([['a', 'b'], ['c', 'd'], ['a', 'd']], 
                                [2, 3, 6], 
                                [['b', 'c'], ['d', 'b'], ['a', 'a']]))