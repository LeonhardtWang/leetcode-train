# 方法一：暴力法（超时）
class Solution:
    def grayCode(self, n: int) -> list:
        num_set = {i for i in range(1, 2**n)}
        res = [0]
        while len(res) != 2 ** n:
            while num_set:
                for num in num_set:
                    if num not in res and self.count_dis_bits(res[-1], num) == 1:
                        res.append(num)
                        num_set.remove(num)
                        break
        return res

    def count_dis_bits(self, a, b):
        count = 0
        while a or b:
            count += a & 1 != b & 1
            a >>= 1
            b >>= 1
        return count

# 方法二：动态规划(递归)
class Solution2:
    def grayCode(self, n: int) -> list:
        if n == 0:
            return [0]
        else:
            pre = self.grayCode(n-1)
            res = [p for p in pre]
            for i in reversed(range(len(pre))):
                res.append(2**(n-1)+pre[i])
            return res

# 方法三：动态规划（循环）
class Solution3:
    def grayCode(self, n: int) -> list:
        n_i, pre = 1, [0]
        while n_i <= n:
            res = [p for p in pre]
            for i in reversed(range(len(pre))):
                res.append(2**(n_i-1)+pre[i])
            pre = [r for r in res]
            n_i += 1
        return pre

print(Solution3().grayCode(2))