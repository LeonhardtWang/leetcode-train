# 方法：扫描线法
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from functools import cmp_to_key
        import bisect
        def cmp(x, y):
            if x[0] - y[0] < 0:
                return -1
            elif x[0] - y[0] > 0:
                return 1
            else:
                if x[1] - y[1] < 0:
                    return 1
                elif x[1] - y[1] > 0:
                    return -1
                else:
                    return 0
        
        l_r_lis = []
        for l, r, h in buildings:
            l_r_lis.append((l, h))
            l_r_lis.append((r, -h)) # 负数表示右端点
        l_r_lis.sort(key=cmp_to_key(cmp))
        max_h = 0
        res = []
        heap = [0]
        for x, y in l_r_lis:
            if y > 0:
                bisect.insort(heap, y)
            else:
                heap.remove(-y)
            curr_max_h = heap[-1]
            if curr_max_h != max_h:
                res.append([x, curr_max_h])
                max_h = curr_max_h
        return res
                
print(Solution().getSkyline([[0,2,3],[2,5,3]]))
