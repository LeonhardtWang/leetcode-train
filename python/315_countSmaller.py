# 方法一：暴力法（超时）
class Solution:
    def countSmaller(self, nums: list) -> list:
        n = len(nums)
        counts = [0 for _ in range(n)]
        for i in range(n-1):
            count = 0
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    count += 1
            counts[i] = count
        return counts

# 方法二：二分查找+插入排序
class Solution2:
    def countSmaller(self, nums: list) -> list:
        import bisect
        n = len(nums)
        ins = []
        ans = [0] * n
        for i in range(n-1, -1, -1):
            index = bisect.bisect_left(ins, nums[i])
            ans[i] = index
            bisect.insort_left(ins, nums[i])
        return ans

# 方法三：归并排序算逆序数
class Solution3:
    def countSmaller(self, nums: list) -> list:
        size = len(nums)
        if not size:
            return []
        nums = [(i, v) for i, v in enumerate(nums)]
        self.result = [0] * size
        self.merge_sort(nums)
        return self.result
        
    def merge_sort(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        
        tmp = []
        
        left_n = len(left)
        right_n = len(right)
        l = 0
        r = 0
        count_r = 0
        while l < left_n and r < right_n:
            if left[l][1] <= right[r][1]:
                self.result[left[l][0]] += count_r
                tmp.append(left[l])
                l += 1
            else:
                tmp.append(right[r])
                r += 1
                count_r += 1
        while l < left_n:
            self.result[left[l][0]] += count_r
            tmp.append(left[l])
            l += 1
        while r < right_n:
            tmp.append(right[r])
            r += 1
        return tmp

# 方法四：排序树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 0 # 纪录左子树的节点
        self.left = None
        self.right = None
        
class Solution4:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = [0] * len(nums)
        root = None
        for i in reversed(range(len(nums))):
            root = self.insert(root, nums[i], res, i)
        return res

    def insert(self, root, val, res, index):
        if root is None:
            root = TreeNode(val)
        elif val <= root.val:
            root.left = self.insert(root.left, val, res, index)
            root.count += 1
        else:
            root.right = self.insert(root.right, val, res, index)
            res[index] += root.count + 1
        return root
    
print(Solution3().countSmaller([4, 2, 1, 2, 5, 5, 3]))