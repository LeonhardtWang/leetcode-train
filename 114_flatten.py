# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            right_node = root.left
            if right_node:
                while right_node.right:
                    right_node = right_node.right
                right_node.right = root.right
                root.right = root.left
            root.left = None
            root = root.right