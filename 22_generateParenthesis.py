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


print(Solutin().generateParenthesis(3))