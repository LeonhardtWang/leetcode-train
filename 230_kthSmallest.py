# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        return self.Core(root)
    
    def Core(self, root):
        if not root:
            return
        left = self.Core(root.left)
        if left is not None:
            return left
        self.k -= 1
        if self.k == 0:
            return root.val
        right = self.Core(root.right)
        if right is not None:
            return right