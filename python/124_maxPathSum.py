# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        def helper(root):
            nonlocal max_sum
            if not root:
                return 0
            left_gain = max(helper(root.left), 0)
            right_gain = max(helper(root.right), 0)
            
            max_sum = max(max_sum, left_gain+right_gain+root.val)
            
            return root.val + max(left_gain, right_gain)
            
            
        helper(root)
        return max_sum
