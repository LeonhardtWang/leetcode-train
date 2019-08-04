# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return (self._helper(root, sum) + 
                self.pathSum(root.left, sum) + 
                self.pathSum(root.right, sum))
        
    def _helper(self, root, sum):
        if not root:
            return 0
        left = self._helper(root.left, sum-root.val)
        right = self._helper(root.right, sum-root.val)
        return left + right + (root.val == sum)