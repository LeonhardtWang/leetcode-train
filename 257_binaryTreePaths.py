# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 递归
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        
        paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        
        for i in range(len(paths)):
            paths[i] = str(root.val) + '->' + paths[i]
        
        return paths