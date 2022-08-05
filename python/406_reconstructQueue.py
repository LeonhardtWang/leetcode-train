class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_add_i = [[i] + p for i, p in enumerate(people)]
        res = []
        while people_add_i:
            min_p = (0, float('inf'), 0)
            min_i = -1
            for i, p in enumerate(people_add_i):
                if p[2] == 0:
                    if p[1] < min_p[1]:
                        min_p = p
                        min_i = i
            
            res.append(people[min_p[0]])
            del people_add_i[min_i]
            for p in people_add_i:
                if p[1] <= min_p[1]:
                    p[2] -= 1
        return res
            
            
print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))