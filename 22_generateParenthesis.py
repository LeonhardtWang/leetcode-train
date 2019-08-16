class Solutin:
    def generateParenthesis(self, n: int) -> list:
        if n == 0:
            return []
        res = [['']]
        for i in range(1, n+1):
            tmp = []
            for p in range(i):
                q = i - p - 1
                p_res_lis = res[p]
                q_res_lis = res[q]
                for p_res in p_res_lis:
                    for q_res in q_res_lis:
                        cur = '(' + p_res + ')' + q_res
                        tmp.append(cur)
            res.append(tmp)
        return res[n]

# 方法二：递归
class Solutin2:
    def generateParenthesis(self, n):
        self.result = []
        if n == 0:
            return self.result
        self._gen(0, 0, n, '')
        return self.result
        
    def _gen(self, left, right, n, result):
        if left == right == n:
            self.result.append(result)
            return 
        if left < n:
            self._gen(left+1, right, n, result+'(')
        if left > right and right < n:
            self._gen(left, right+1, n, result+')')

print(Solutin2().generateParenthesis(4))