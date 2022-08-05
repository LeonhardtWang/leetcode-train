# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p) and (not q):
            return True
        elif (not p) + (not q) == 1:
            return False
        if p.val == q.val: # 递归解决
            left_res = self.isSameTree(p.left, q.left)
            right_res = self.isSameTree(p.right, q.right)
            return left_res and right_res
        else:
            return False