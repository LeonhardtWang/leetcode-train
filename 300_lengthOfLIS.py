# 方法一：动态规划
class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        for i in range(n):
            curr = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    curr = max(curr, dp[j])
            dp[i] = curr + 1
            res = max(res, dp[i])
        return res

# 方法二：二分查找
class Solution2:
    def lengthOfLIS(self, nums: list) -> int:
        ans = []
        for num in nums:
            lo = 0
            hi = len(ans) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if ans[mid] < num:
                    lo = mid + 1
                elif ans[mid] > num:
                    hi = mid - 1
                else:
                    lo = mid
                    break
            if lo == len(ans):
                ans.append(num)
            else:
                ans[lo] = num
        return len(ans)

print(Solution2().lengthOfLIS([10,9,2,5,3,7,101,18]))
            