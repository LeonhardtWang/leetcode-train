class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            res_in = []
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                for k in range(len(res[-1])):
                    if k == len(res[-1]) - 1:break
                    res_in.append(res[-1][k] + res[-1][k+1])
                res_in.insert(0, 1);res_in.insert(len(res_in), 1)
                res.append(res_in)
        return res[rowIndex]
            