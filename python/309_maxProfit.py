class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_1_0 = 0
        dp_i_1_1 = float('-inf')
        dp_i_2_0 = 0
        for i, p in enumerate(prices):
            tmp = dp_i_1_0
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1+p)
            dp_i_1_1 = max(dp_i_1_1, dp_i_2_0-p)
            dp_i_2_0 = tmp
        return dp_i_1_0