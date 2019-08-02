# 方法一：递归（时间复杂度过高）
class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        res = float('inf')
        for coin in coins:
            next_amount = amount - coin
            if next_amount >= 0:
                next_res = self.coinChange(coins, next_amount)
                if next_res != -1:
                    res = min(res, next_res + 1) 
        return res if res != float('inf') else -1

# 方法二：递归+备忘录
class Solution2:
    def __init__(self):
        self.cou_res_dic = {} # 备忘录法
    def coinChange(self, coins: list, amount: int) -> int:
        if amount == 0:
            return 0
        res = float('inf')
        for coin in coins:
            next_amount = amount - coin
            if next_amount >= 0:
                if next_amount in self.cou_res_dic:
                    next_res = self.cou_res_dic[next_amount]
                else:
                    next_res = self.coinChange(coins, next_amount)
                    self.cou_res_dic[next_amount] = next_res
                if next_res != -1:
                    res = min(res, next_res + 1) 
        return res if res != float('inf') else -1

# 方法三：动态规划
class Solution3:
    def coinChange(self, coins: list, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
print(Solution3().coinChange([2,5,10,1], 27))
