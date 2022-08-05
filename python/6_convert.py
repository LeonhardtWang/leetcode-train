class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        s_lis = [[] for _ in range(numRows)]
        for i, ch in enumerate(s):
            index = i % (2 * numRows - 2)
            if index == 0:
                index_T = 0
                dirc = '+'
            if index == numRows - 1:
                dirc = '-'
            s_lis[index_T].append(ch)
            if dirc == '+':
                index_T += 1
            else:
                index_T -= 1
        res = ''
        for i in s_lis:
            for j in i:
                res += j
        return res
            