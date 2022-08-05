def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 定义函数f(n)，为以第n个数为结束点的子数列的最大和
    # 存在递推关系：f(n) = max(f(n-1) + A[n], A[n])
    for i in range(1, len(nums)):
        if nums[i-1] + nums[i] > nums[i]:
            nums[i] = nums[i-1] + nums[i]
    return max(nums)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))