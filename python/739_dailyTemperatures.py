# 方法一：暴力法（超时）
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = []
        for i, t in enumerate(T):
            tmp = 0
            j = i + 1
            while j < len(T):
                if T[j] > t:
                    tmp += j - i
                    break
                j += 1
            res.append(tmp)
        return res

# 方法二：去掉暴力法中重复遍历的部分（从后往前）
class Solution2(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        dp = [0 for _ in range(len(T))]
        for i in range(len(T)-1, -1, -1):
            j = i + 1
            while j < len(T):
                if T[j] > T[i]:
                    dp[i] = j - i
                    break
                elif T[j] <= T[i] and dp[j] != 0:
                    j += dp[j]
                else:
                    break
        return dp

print(Solution2().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))