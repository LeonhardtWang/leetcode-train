# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        left = self._helper(root.left)
        right = self._helper(root.right)
        
        cross_mid = left + right # 过根节点
        left_no_cross_mid = self.diameterOfBinaryTree(root.left)
        right_no_cross_mid = self.diameterOfBinaryTree(root.right)
        return max(cross_mid, left_no_cross_mid, right_no_cross_mid)
        
    def _helper(self, root):
        # 算出最大深度
        if not root:
            return 0
        left = self._helper(root.left)
        right = self._helper(root.right)
        return max(left, right) + 1